from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        indexToName = {}
        indexToEmails = defaultdict(set)
        emailToIndex = {}

        for index, account in enumerate(accounts):
            indexToName[index] = account[0]
            account[0] = index

        for account in accounts:
            index = account[0]
            emails = account[1:]
            seenEmails = [email for email in emails if email in emailToIndex]
            indexes = set([index] + [emailToIndex[email] for email in seenEmails])
            indexes = sorted(indexes, key=lambda index: len(indexToEmails[index]), reverse=True)
            new_index = indexes[0]
            for old_index in indexes[1:]:
                old_emails = indexToEmails[old_index]
                for email in old_emails:
                    emailToIndex[email] = new_index
                indexToEmails[new_index].update(old_emails)
                del indexToEmails[old_index]
            for email in emails:
                indexToEmails[new_index].add(email)
                emailToIndex[email] = new_index

        return [[indexToName[index]] + sorted(indexToEmails[index]) for index in indexToEmails.keys()]   