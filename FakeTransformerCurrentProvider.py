from TransformerCurrentProvider import TransformerCurrentProvider


class FakeTransformerCurrentProvider(TransformerCurrentProvider):
    ValueToReturn = 0.1

    def GetCurrent(self):
        return self.ValueToReturn
