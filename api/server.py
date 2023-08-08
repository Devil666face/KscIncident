import urllib3
import socket

from utils.logger import logger as l

from KlAkOAPI.AdmServer import KlAkAdmServer
from KlAkOAPI.SrvView import KlAkSrvView
from KlAkOAPI.Base import KlAkArray


class KscServer:
    def __init__(
        self,
        ip: str,
        username: str,
        password: str,
        port: int = 13299,
    ) -> None:
        urllib3.disable_warnings()
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.server_url = f"https://{socket.getfqdn(self.ip)}:{self.port}"
        try:
            self.server = KlAkAdmServer.Create(
                self.server_url,
                self.username,
                self.password,
                verify=False,
            )
        except ConnectionError as err:
            l.exception(err)

    @property
    def events(self) -> None:
        """
        [Sample](https://support.kaspersky.com/help/KSC/13.2/KSCAPI/a00438.html)
        [Srvview list](https://support.kaspersky.com/help/KSC/13.2/KSCAPI/a00153.html)
        [List of attributes for events](https://support.kaspersky.com/help/KSC/13.2/KSCAPI/a00207.html)
        [List of attributes for events](https://support.kaspersky.com/help/KSC/13.2/KSCAPI/a00127.html)
        event_type:
        - "KLPRCI_TaskState" - изменено состояние задачи. Смотрите атрибут "task_new_state".
        - "GNRL_EV_SUSPICIOUS_OBJECT_FOUND" - Обнаружен подозрительный объект.
        - "GNRL_EV_VIRUS_FOUND" - вирус найден.
        - "GNRL_EV_OBJECT_CURED" - Объект был вылечен.
        - "GNRL_EV_OBJECT_DELETED" - Объект был удален.
        - "GNRL_EV_OBJECT_REPORTED" - Объект был зарегистрирован.
        - Найден "GNRL_EV_PASSWD_ARCHIVE_FOUND" - архив, защищенный паролем.
        - "GNRL_EV_OBJECT_QUARANTINED" - Объект был помещен в карантин.
        - "GNRL_EV_OBJECT_NOTCURED" - Объект не был вылечен.
        - [Another](https://support.kaspersky.com/help/KSC/13.2/KSCAPI/a00477.html)
        Ordering:
        - Name: имя поля для сортировки
        - Asc: True-по возрастанию/False-по убыванию
        [Find attrs](https://support.kaspersky.com/help/KSC/13.2/KSCAPI/a00003.html)
        """
        srv_processor = KlAkSrvView(self.server)

        srvview = "EventsSrvViewName"

        fields_to_return = KlAkArray(
            [
                "event_db_id",
                "rise_time",
                "registration_time",
                "KLEVP_EVENT_HOST_IP_ADDRESS",
                "event_type_display_name",
                "GNRL_EA_DESCRIPTION",
                "KLEVP_EVENT_HOST_NETBIOSNAME",
                "event_type",
            ]
        )

        fields_to_order = KlAkArray([{"Name": "rise_time", "Asc": False}])
        find_attrs = {
            # "KLSRVH_SLAVE_REC_DEPTH": 0
            "KLGRP_FIND_FROM_CUR_VS_ONLY": False
        }

        srv_iterator_id = srv_processor.ResetIterator(
            srvview,
            "",
            fields_to_return,
            fields_to_order,
            find_attrs,
            lifetimeSec=60 * 60 * 3,
        ).OutPar("wstrIteratorId")
        # record_count = srv_processor.GetRecordCount(srv_iterator_id).RetVal()
        # for i in range(0, int(record_count), 10000):
        i = 0
        record_range = srv_processor.GetRecordRange(srv_iterator_id, i, i + 100).OutPar(
            "pRecords"
        )
        for record in record_range["KLCSP_ITERATOR_ARRAY"]:
            l.debug(str(record))
        # print(record_count)
