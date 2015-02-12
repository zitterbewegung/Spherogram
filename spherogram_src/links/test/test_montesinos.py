import snappy
import random
from spherogram import RationalTangle

knots = [['4_1', [(2, 5)]], ['5_2', [(3, 7)]], ['6_1', [(4, 9)]], ['6_2', [(4, 11)]], ['6_3', [(5, 13)]], ['7_2', [(5, 11)]], ['7_3', [(4, 13)]], ['7_4', [(4, 15)]], ['7_5', [(7, 17)]], ['7_6', [(7, 19)]], ['7_7', [(8, 21)]], ['8_1', [(6, 13)]], ['8_2', [(6, 17)]], ['8_3', [(4, 17)]], ['8_4', [(5, 19)]], ['8_5', [(1, 3), (1, 3), (1, 2)]], ['8_6', [(10, 23)]], ['8_7', [(9, 23)]], ['8_8', [(9, 25)]], ['8_9', [(7, 25)]], ['8_10', [(1, 3), (2, 3), (1, 2)]], ['8_11', [(10, 27)]], ['8_12', [(12, 29)]], ['8_13', [(11, 29)]], ['8_14', [(12, 31)]], ['8_15', [(2, 3), (2, 3), (1, 2)]], ['8_20', [(1, 3), (2, 3), (-1, 2)]], ['8_21', [(2, 3), (2, 3), (-1, 2)]], ['9_2', [(7, 15)]], ['9_3', [(6, 19)]], ['9_4', [(5, 21)]], ['9_5', [(6, 23)]], ['9_6', [(11, 27)]], ['9_7', [(13, 29)]], ['9_8', [(11, 31)]], ['9_9', [(9, 31)]], ['9_10', [(10, 33)]], ['9_11', [(14, 33)]], ['9_12', [(13, 35)]], ['9_13', [(10, 37)]], ['9_14', [(14, 37)]], ['9_15', [(16, 39)]], ['9_16', [(1, 3), (1, 3), (3, 2)]], ['9_17', [(14, 39)]], ['9_18', [(17, 41)]], ['9_19', [(16, 41)]], ['9_20', [(15, 41)]], ['9_21', [(18, 43)]], ['9_22', [(3, 5), (1, 3), (1, 2)]], ['9_23', [(19, 45)]], ['9_24', [(1, 3), (2, 3), (3, 2)]], ['9_25', [(2, 5), (2, 3), (1, 2)]], ['9_26', [(18, 47)]], ['9_27', [(19, 49)]], ['9_28', [(2, 3), (2, 3), (3, 2)]], ['9_30', [(3, 5), (2, 3), (1, 2)]], ['9_31', [(21, 55)]], ['9_35', [(1, 3), (1, 3), (1, 3)]], ['9_36', [(2, 5), (1, 3), (1, 2)]], ['9_37', [(1, 3), (2, 3), (2, 3)]], ['9_42', [(2, 5), (1, 3), (-1, 2)]], ['9_43', [(3, 5), (1, 3), (-1, 2)]], ['9_44', [(2, 5), (2, 3), (-1, 2)]], ['9_45', [(3, 5), (2, 3), (-1, 2)]], ['9_46', [(1, 3), (1, 3), (-1, 3)]], ['9_48', [(2, 3), (2, 3), (-1, 3)]], ['10_1', [(8, 17)]], ['10_2', [(8, 23)]], ['10_3', [(6, 25)]], ['10_4', [(7, 27)]], ['10_5', [(13, 33)]], ['10_6', [(16, 37)]], ['10_7', [(16, 43)]], ['10_8', [(6, 29)]], ['10_9', [(11, 39)]], ['10_10', [(17, 45)]], ['10_11', [(13, 43)]], ['10_12', [(17, 47)]], ['10_13', [(22, 53)]], ['10_14', [(22, 57)]], ['10_15', [(19, 43)]], ['10_16', [(14, 47)]], ['10_17', [(9, 41)]], ['10_18', [(23, 55)]], ['10_19', [(14, 51)]], ['10_20', [(16, 35)]], ['10_21', [(16, 45)]], ['10_22', [(13, 49)]], ['10_23', [(23, 59)]], ['10_24', [(24, 55)]], ['10_25', [(24, 65)]], ['10_26', [(17, 61)]], ['10_27', [(27, 71)]], ['10_28', [(19, 53)]], ['10_29', [(26, 63)]], ['10_30', [(26, 67)]], ['10_31', [(25, 57)]], ['10_32', [(29, 69)]], ['10_33', [(18, 65)]], ['10_34', [(13, 37)]], ['10_35', [(20, 49)]], ['10_36', [(20, 51)]], ['10_37', [(23, 53)]], ['10_38', [(25, 59)]], ['10_39', [(22, 61)]], ['10_40', [(29, 75)]], ['10_41', [(26, 71)]], ['10_42', [(31, 81)]], ['10_43', [(27, 73)]], ['10_44', [(30, 79)]], ['10_45', [(34, 89)]], ['10_46', [(1, 5), (1, 3), (1, 2)]], ['10_47', [(1, 5), (2, 3), (1, 2)]], ['10_48', [(4, 5), (1, 3), (1, 2)]], ['10_49', [(4, 5), (2, 3), (1, 2)]], ['10_50', [(3, 7), (1, 3), (1, 2)]], ['10_51', [(3, 7), (2, 3), (1, 2)]], ['10_52', [(4, 7), (1, 3), (1, 2)]], ['10_53', [(4, 7), (2, 3), (1, 2)]], ['10_54', [(2, 7), (1, 3), (1, 2)]], ['10_55', [(2, 7), (2, 3), (1, 2)]], ['10_56', [(5, 7), (1, 3), (1, 2)]], ['10_57', [(5, 7), (2, 3), (1, 2)]], ['10_58', [(2, 5), (2, 5), (1, 2)]], ['10_59', [(2, 5), (3, 5), (1, 2)]], ['10_60', [(3, 5), (3, 5), (1, 2)]], ['10_61', [(1, 4), (1, 3), (1, 3)]], ['10_62', [(1, 4), (1, 3), (2, 3)]], ['10_63', [(1, 4), (2, 3), (2, 3)]], ['10_64', [(3, 4), (1, 3), (1, 3)]], ['10_65', [(3, 4), (1, 3), (2, 3)]], ['10_66', [(3, 4), (2, 3), (2, 3)]], ['10_67', [(2, 5), (1, 3), (2, 3)]], ['10_68', [(3, 5), (1, 3), (1, 3)]], ['10_69', [(3, 5), (2, 3), (2, 3)]], ['10_70', [(2, 5), (1, 3), (3, 2)]], ['10_71', [(2, 5), (2, 3), (3, 2)]], ['10_72', [(3, 5), (1, 3), (3, 2)]], ['10_73', [(3, 5), (2, 3), (3, 2)]], ['10_74', [(1, 3), (1, 3), (5, 3)]], ['10_75', [(2, 3), (2, 3), (5, 3)]], ['10_76', [(1, 3), (1, 3), (5, 2)]], ['10_77', [(1, 3), (2, 3), (5, 2)]], ['10_78', [(2, 3), (2, 3), (5, 2)]], ['10_125', [(1, 5), (2, 3), (-1, 2)]], ['10_126', [(4, 5), (1, 3), (-1, 2)]], ['10_127', [(4, 5), (2, 3), (-1, 2)]], ['10_128', [(3, 7), (1, 3), (-1, 2)]], ['10_129', [(3, 7), (2, 3), (-1, 2)]], ['10_130', [(4, 7), (1, 3), (-1, 2)]], ['10_131', [(4, 7), (2, 3), (-1, 2)]], ['10_132', [(2, 7), (1, 3), (-1, 2)]], ['10_133', [(2, 7), (2, 3), (-1, 2)]], ['10_134', [(5, 7), (1, 3), (-1, 2)]], ['10_135', [(5, 7), (2, 3), (-1, 2)]], ['10_136', [(2, 5), (2, 5), (-1, 2)]], ['10_137', [(2, 5), (3, 5), (-1, 2)]], ['10_138', [(3, 5), (3, 5), (-1, 2)]], ['10_139', [(1, 4), (1, 3), (-2, 3)]], ['10_140', [(1, 4), (1, 3), (-1, 3)]], ['10_141', [(1, 4), (2, 3), (-1, 3)]], ['10_142', [(3, 4), (1, 3), (-2, 3)]], ['10_143', [(3, 4), (1, 3), (-1, 3)]], ['10_144', [(3, 4), (2, 3), (-1, 3)]], ['10_145', [(2, 5), (1, 3), (-2, 3)]], ['10_146', [(2, 5), (2, 3), (-1, 3)]], ['10_147', [(3, 5), (1, 3), (-1, 3)]]]

def knot(fractions):
    if len(fractions) == 1:
        return RationalTangle(*fractions[0]).denominator_closure()
    else:
        A, B, C = [RationalTangle(*f) for f in fractions]
        T = A + B + C
        return T.numerator_closure()

def test(N=len(knots)):
    for name, fractions in random.sample(knots, N):
        K = knot(fractions)
        M0, M1 = K.exterior(), snappy.Manifold(K.DT_code(True))
        N0 = snappy.LinkExteriors.identify(M0)
        N1 = snappy.LinkExteriors.identify(M1)
        assert N0.name() == name and N1.name() == name
