import urllib3
import socket

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
        except ConnectionError as ex:
            print(ex)

    @property
    def events(self) -> None:
        # [Sample](https://support.kaspersky.com/help/KSC/13.2/KSCAPI/a00438.html)
        srv_processor = KlAkSrvView(self.server)

        # [Srvview list](https://support.kaspersky.com/help/KSC/13.2/KSCAPI/a00153.html)
        srvview = "EventsSrvViewName"

        # [List of attributes for events](https://support.kaspersky.com/help/KSC/13.2/KSCAPI/a00207.html)
        # [List of attributes for events](https://support.kaspersky.com/help/KSC/13.2/KSCAPI/a00127.html)
        fields_to_return = KlAkArray(
            [
                "rise_time",
                "KLEVP_EVENT_HOST_IP_ADDRESS",
                "event_type_display_name",
            ]
        )

        # Name: название поля для сортировки
        # Asc: True-по возрастанию/False-по убыванию
        fields_to_order = KlAkArray([{"Name": "rise_time", "Asc": False}])

        # [Find attrs](https://support.kaspersky.com/help/KSC/13.2/KSCAPI/a00003.html)
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
        record_count = srv_processor.GetRecordCount(srv_iterator_id).RetVal()

        # for i in range(0, int(record_count), 10000):
        record_range = srv_processor.GetRecordRange(
            srv_iterator_id, i, i + 10000
        ).OutPar("pRecords")
        for record in record_range["KLCSP_ITERATOR_ARRAY"]:
            print(record)
        print(record_count)
