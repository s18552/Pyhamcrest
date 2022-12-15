import json
import math

import pytest as pytest


def statement(invoice, plays):
    total_amount = 0
    volume_credits = 0
    result = f'Statement for {invoice["customer"]}\n'

    def format_as_dollars(amount):
        return f"${amount:0,.2f}"

    for perf in invoice['performances']:
        play = plays[perf['playID']]
        if play['type'] == "tragedy":
            this_amount = 40000
            if perf['audience'] > 30:
                this_amount += 1000 * (perf['audience'] - 30)
        elif play['type'] == "comedy":
            this_amount = 30000
            if perf['audience'] > 20:
                this_amount += 10000 + 500 * (perf['audience'] - 20)

            this_amount += 300 * perf['audience']
        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf['audience'] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf['audience'] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount / 100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f'Amount owed is {format_as_dollars(total_amount / 100)}\n'
    result += f'You earned {volume_credits} credits\n'
    print(result)
    print(type(result))
    return result


if __name__ == "__main__":
    statement({"customer": "BigCo",
               "performances": [{"playID": "hamlet", "audience": 55}, {"playID": "as-like", "audience": 35},
                                {"playID": "othello", "audience": 40}]}, {
                  "hamlet": {"name": "Hamlet", "type": "tragedy"},
                  "as-like": {"name": "As You Like It", "type": "comedy"},
                  "othello": {"name": "Othello", "type": "tragedy"}
              })


import unittest



class Test(unittest.TestCase):



    def test_earned_money(self):
        self.assertTrue("$400" in statement({"customer": "BigCo",
                                             "performances": [{"playID": "hamlet", "audience": 15}]},
                                            {
                                                "hamlet": {"name": "Hamlet", "type": "tragedy"}},
                                            ))

    def test_play_amount_hamlet_and_as_like(self):
        self.assertTrue("1,210" in statement({"customer": "BigCo",
                                              "performances": [{"playID": "hamlet", "audience": 45},
                                                               {"playID": "as-like", "audience": 45}]},
                                             {
                                                 "hamlet": {"name": "Hamlet", "type": "tragedy"},
                                                 "as-like": {"name": "As You Like It", "type": "comedy"}}))


    def test_credits_for_othello(self):
        self.assertTrue("10" in statement({"customer": "BigCo",
                                              "performances": [{"playID": "othello", "audience": 40}]},
                                             {
                                                 "othello": {"name": "Othello", "type": "tragedy"}}))

    def test_credits_for_as_like(self):
        self.assertTrue("12" in statement({"customer": "BigCo",
                                              "performances": [{"playID": "as-like", "audience": 35}]},
                                             {
                                                 "as-like": {"name": "As You Like It", "type": "comedy"}
                                             }))

    def test_audience_for_as_like(self):
        self.assertTrue("100" in statement({"customer": "BigCo",
                                              "performances": [{"playID": "as-like", "audience": 100}]},
                                             {
                                                 "as-like": {"name": "As You Like It", "type": "comedy"}
                                             }))


