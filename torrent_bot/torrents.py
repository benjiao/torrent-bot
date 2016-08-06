import json
import transmissionrpc


class Torrents:
    def __init__(self):
        self.tc = transmissionrpc.Client(address='localhost', port=9091)
        self.torrent_session = self.tc.get_session()

    def get_torrents(self):
        results = self.tc.get_torrents()
        torrent_list = []

        for result in results:
            torrent_list.append({
                'hash': result.hashString,
                'eta': result.format_eta(),
                'status': result.status,
                'progress': result.progress,
                'files': [val for key, val in result.files().iteritems()]
            })

        return torrent_list

    def pause_all(self):
        results = self.tc.get_torrents()

        for result in results:
            result.stop()

        return True

    def resume_all(self):
        results = self.tc.get_torrents()

        for result in results:
            result.start()

        return True

if __name__ == '__main__':
    tc = Torrents()
    results = tc.get_torrents()
    print json.dumps(results, indent=4)