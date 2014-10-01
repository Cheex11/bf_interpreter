import unfucker
import unittest


# unfucker.quick_add(3,2)

class TestUF(unittest.TestCase):

    def setUp(self):
        self.defined_bf_x = '++++++++[>+++++++++++<-]>.'


    # def test_output(self):
    #     self.output_x = unfucker.output(self.defined_bf_x)
    #     self.assertEqual('x', self.output_x)

    # def test_read(self):
    #     self.read_file = unfucker.open_and_read_file('bf_x.txt')
    #     self.assertEqual(self.read_file, self.defined_bf_x)


    # def test_shuffle(self):
    #     # make sure the shuffled sequence does not lose any elements
    #     random.shuffle(self.seq)
    #     self.seq.sort()
    #     self.assertEqual(self.seq, range(10))

    #     # should raise an exception for an immutable sequence
    #     self.assertRaises(TypeError, random.shuffle, (1,2,3))

    # def test_choice(self):
    #     element = random.choice(self.seq)
    #     self.assertTrue(element in self.seq)

    # def test_sample(self):
    #     with self.assertRaises(ValueError):
    #         random.sample(self.seq, 20)
    #     for element in random.sample(self.seq, 5):
    #         self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()

