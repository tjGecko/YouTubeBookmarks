from datetime import datetime


class VideoBookmark:
    def __init__(self):
        # See: https://www.freecodecamp.org/news/author/patrick-collins/
        # Great tutorials Patrick!
        self.video_url = 'https://www.youtube.com/watch?v=M576WGiDBdQ&t={}s'    # URL with position placeholder

        self.bookmarks = {
            'L13: Map blockchain id to config for token addresses': '14:43:32',
            'L13: Query brownie config for blockchain networks': '14:34:45',
            'L13: useDapp: Import header component': '14:26:28',
            'L13: useDapp: Configure supported chains': '14:20:00',
            'L13: useDapp': '14:16:30',
            'L13: React Project Layout': '14:12:00',
            'L13: TestNet: Front End: Yarn Install': '14:10:10',
            'L13: TestNet: Front End: Create React App': '14:09:48',
            'L13: Test: Issue tokens2': '14:05:10',
            'L13: Test: Issue tokens': '14:03:15',
            'L13: Test: Stake tokens': '14:00:15',
            'L13: Test 2: Issue token farm tokens': '13:55:00',
            'L13: Test token farm': '13:48:30',
            'L13: Add allowed tokens to token farm': '13:46:00',
            'L13: Add fake tokens for staking': '13:37:00',
            'L13: Add mocks': '13:31:00',
            'L13: ReEntrance attack?': '13:27:50',
            'L13: Chainlink Price Feeds': '13:19:00',
            'L13: getUserTotalValue': '13:13:00',
            'L13: Issue Incentive Tokens': '13:07:00',
            'L13: Define Dapp Token': '12:53:43',
            'Full Stack: Lesson 13': '12:52:35',
            'TestNet: Proxy Deploy: Etherscan': '12:45:41',
            'TestNet: Proxy Deploy': '12:43:41',
            'Smart Contract: Proxy: Tests': '12:33:10',
            'Smart Contract: Proxy: Assign ABI': '12:21:15',
            'Smart Contract: Proxy: Encode Initializer': '12:16:00',
            'Smart Contract: Proxy Admin': '12:13:00',
            'Smart Contract: Proxy: Initial Deploy Script': '12:10:30',
            'Smart Contract: Proxy: External Contract Relative Path Edits': '12:06:30',
            'Smart Contract: Proxy: Transparent Proxy Pattern': '12:00:00',
            'Smart Contract: Proxy: Proxy Contract': '11:57:14',
            'Smart Contract: Proxy: Implementation Contract': '11:57:00',
            'Smart Contract: Upgrades.Proxies': '11:55:10',
            'Smart Contract: Upgrades.Migration': '11:53:00',
            'Smart Contract: Upgrades.Setters': '11:50:50',
            'Smart Contract: Integration Testing.2': '11:44:00',
            'Smart Contract: Integration Testing': '11:43:28',
            'Smart Contract.set Token URI Manually': '11:39:10',
            'IPFS Upload: Pinata2': '11:30:00',
            'IPFS Upload: Pinata': '11:24:30',
            'IPFS Cmd line API and personal ipfs node': '11:17:42',
            'IPFS Check IP location': '11:17:00',
            'IPFS Command line download': '11:16:43',
            'Python: Upload file to IPFS': '11:14:22',
            'Assign Metadata and set up for IPFS': '11:05:40',
            'Start IPFS/Mention FileCoin': '11:02:40',
            'Random dog breed': '11:00:00',
            'NFT: Start': '9:50:20',
        }

    def get_bookmark(self, key: str):
        youtube_time = self.bookmarks[key]
        date = datetime.strptime(youtube_time, '%H:%M:%S')
        hr_sec = 60**2 * date.hour
        min_sec = 60**1 * date.minute
        total_sec = hr_sec + min_sec + date.second

        print(f'URL: {self.video_url.format(total_sec)}')


if __name__ == '__main__':
    vb = VideoBookmark()
    vb.get_bookmark(key='NFT: Start')
    
