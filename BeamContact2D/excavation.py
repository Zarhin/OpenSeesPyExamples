#######################################################################
#                                                                     #
#  Excavation of cohesionless soil supported by a cantilevered sheet  #
#  pile wall.  2D Plane Strain analysis.  Beam elements define the    #
#  wall, and beam-contact elements are used to create a frictional    #
#  soil-pile interface. Initial state analysis is used to create      #
#  an initial state of stress and strain due to gravity without the   #
#  corresponding displacements.                                       #
#                                                                     #
#   Created by:  Chris McGann                                         #
#                Pedro Arduino                                        #
#              --University of Washington--                           #
#                                                                     #
# ---> Basic units are kN and m                                       #
#                                                                     #
#######################################################################

import openseespy.opensees as ops
import numpy as np
import opensees_to_gid as otg

ops.wipe()

# -----------------------------------------------------------------------------------------
#  1. CREATE SOIL NODES AND FIXITIES
# -----------------------------------------------------------------------------------------
ops.model('BasicBuilder', '-ndm', 2, '-ndf', 2)

# define soil nodes
ops.node(1, -5.250, 0.000)
ops.node(2, -5.250, 0.500)
ops.node(3, -4.750, 0.000)
ops.node(4, -4.750, 0.500)
ops.node(5, -4.250, 0.000)
ops.node(6, -5.250, 1.000)
ops.node(7, -4.750, 1.000)
ops.node(8, -4.250, 0.500)
ops.node(9, -4.250, 1.000)
ops.node(10, -5.250, 1.500)
ops.node(11, -3.750, 0.000)
ops.node(12, -4.750, 1.500)
ops.node(13, -3.750, 0.500)
ops.node(14, -3.750, 1.000)
ops.node(15, -4.250, 1.500)
ops.node(16, -3.250, 0.000)
ops.node(17, -5.250, 2.000)
ops.node(18, -4.750, 2.000)
ops.node(19, -3.250, 0.500)
ops.node(20, -3.750, 1.500)
ops.node(21, -3.250, 1.000)
ops.node(22, -4.250, 2.000)
ops.node(23, -5.250, 2.500)
ops.node(24, -2.750, 0.000)
ops.node(25, -3.250, 1.500)
ops.node(26, -3.750, 2.000)
ops.node(27, -4.750, 2.500)
ops.node(28, -2.750, 0.500)
ops.node(29, -4.250, 2.500)
ops.node(30, -2.750, 1.000)
ops.node(31, -3.250, 2.000)
ops.node(32, -3.750, 2.500)
ops.node(33, -2.750, 1.500)
ops.node(34, -5.250, 3.000)
ops.node(35, -2.250, 0.000)
ops.node(36, -4.750, 3.000)
ops.node(37, -2.250, 0.500)
ops.node(38, -4.250, 3.000)
ops.node(39, -2.250, 1.000)
ops.node(40, -3.250, 2.500)
ops.node(41, -2.750, 2.000)
ops.node(42, -3.750, 3.000)
ops.node(43, -2.250, 1.500)
ops.node(44, -5.250, 3.500)
ops.node(45, -1.750, 0.000)
ops.node(46, -2.750, 2.500)
ops.node(47, -4.750, 3.500)
ops.node(48, -1.750, 0.500)
ops.node(49, -2.250, 2.000)
ops.node(50, -3.250, 3.000)
ops.node(51, -1.750, 1.000)
ops.node(52, -4.250, 3.500)
ops.node(53, -3.750, 3.500)
ops.node(54, -1.750, 1.500)
ops.node(55, -2.250, 2.500)
ops.node(56, -2.750, 3.000)
ops.node(57, -5.250, 4.000)
ops.node(58, -1.250, 0.000)
ops.node(59, -1.250, 0.500)
ops.node(60, -4.750, 4.000)
ops.node(61, -1.750, 2.000)
ops.node(62, -3.250, 3.500)
ops.node(63, -4.250, 4.000)
ops.node(64, -1.250, 1.000)
ops.node(65, -2.250, 3.000)
ops.node(66, -3.750, 4.000)
ops.node(67, -1.250, 1.500)
ops.node(68, -1.750, 2.500)
ops.node(69, -2.750, 3.500)
ops.node(70, -1.250, 2.000)
ops.node(71, -3.250, 4.000)
ops.node(72, -0.750, 0.000)
ops.node(73, -5.250, 4.500)
ops.node(74, -4.750, 4.500)
ops.node(75, -0.750, 0.500)
ops.node(76, -4.250, 4.500)
ops.node(77, -1.750, 3.000)
ops.node(78, -2.250, 3.500)
ops.node(79, -0.750, 1.000)
ops.node(80, -1.250, 2.500)
ops.node(81, -2.750, 4.000)
ops.node(82, -3.750, 4.500)
ops.node(83, -0.750, 1.500)
ops.node(84, -0.750, 2.000)
ops.node(85, -3.250, 4.500)
ops.node(86, -1.750, 3.500)
ops.node(87, -5.250, 5.000)
ops.node(88, -0.250, 0.000)
ops.node(89, -1.250, 3.000)
ops.node(90, -2.250, 4.000)
ops.node(91, -4.750, 5.000)
ops.node(92, -0.250, 0.500)
ops.node(93, -0.250, 1.000)
ops.node(94, -4.250, 5.000)
ops.node(95, -0.750, 2.500)
ops.node(96, -2.750, 4.500)
ops.node(97, -3.750, 5.000)
ops.node(98, -0.250, 1.500)
ops.node(102, -1.750, 4.000)
ops.node(103, -1.250, 3.500)
ops.node(104, -3.250, 5.000)
ops.node(105, -0.250, 2.000)
ops.node(107, -0.750, 3.000)
ops.node(108, -2.250, 4.500)
ops.node(109, 0.250, 0.000)
ops.node(110, -5.250, 5.500)
ops.node(111, -4.750, 5.500)
ops.node(112, 0.250, 0.500)
ops.node(114, -2.750, 5.000)
ops.node(115, -0.250, 2.500)
ops.node(116, 0.250, 1.000)
ops.node(117, -4.250, 5.500)
ops.node(118, -1.250, 4.000)
ops.node(119, 0.250, 1.500)
ops.node(120, -3.750, 5.500)
ops.node(121, -1.750, 4.500)
ops.node(122, -0.750, 3.500)
ops.node(124, -2.250, 5.000)
ops.node(125, -0.250, 3.000)
ops.node(126, 0.250, 2.000)
ops.node(127, -3.250, 5.500)
ops.node(129, -5.250, 6.000)
ops.node(130, 0.750, 0.000)
ops.node(131, 0.750, 0.500)
ops.node(132, -1.250, 4.500)
ops.node(133, -4.750, 6.000)
ops.node(134, -0.750, 4.000)
ops.node(135, 0.250, 2.500)
ops.node(136, -2.750, 5.500)
ops.node(137, -4.250, 6.000)
ops.node(138, 0.750, 1.000)
ops.node(139, -0.250, 3.500)
ops.node(140, -1.750, 5.000)
ops.node(142, -3.750, 6.000)
ops.node(143, 0.750, 1.500)
ops.node(144, 0.250, 3.000)
ops.node(145, -2.250, 5.500)
ops.node(146, 0.750, 2.000)
ops.node(147, -3.250, 6.000)
ops.node(148, -0.750, 4.500)
ops.node(149, -1.250, 5.000)
ops.node(150, -0.250, 4.000)
ops.node(152, 1.250, 0.000)
ops.node(153, 0.750, 2.500)
ops.node(154, -5.250, 6.500)
ops.node(155, -2.750, 6.000)
ops.node(156, -4.750, 6.500)
ops.node(157, 1.250, 0.500)
ops.node(158, 0.250, 3.500)
ops.node(159, -1.750, 5.500)
ops.node(160, -4.250, 6.500)
ops.node(161, 1.250, 1.000)
ops.node(162, 1.250, 1.500)
ops.node(163, -3.750, 6.500)
ops.node(164, 0.750, 3.000)
ops.node(165, -2.250, 6.000)
ops.node(166, -0.250, 4.500)
ops.node(167, -0.750, 5.000)
ops.node(169, -3.250, 6.500)
ops.node(170, 1.250, 2.000)
ops.node(171, 0.250, 4.000)
ops.node(172, -1.250, 5.500)
ops.node(173, 0.750, 3.500)
ops.node(174, -1.750, 6.000)
ops.node(175, -2.750, 6.500)
ops.node(176, 1.250, 2.500)
ops.node(177, -5.250, 7.000)
ops.node(178, 1.750, 0.000)
ops.node(179, -4.750, 7.000)
ops.node(180, 1.750, 0.500)
ops.node(181, 1.750, 1.000)
ops.node(182, -0.250, 5.000)
ops.node(183, -4.250, 7.000)
ops.node(185, 0.250, 4.500)
ops.node(186, -0.750, 5.500)
ops.node(187, 1.750, 1.500)
ops.node(188, -2.250, 6.500)
ops.node(189, 1.250, 3.000)
ops.node(190, -3.750, 7.000)
ops.node(191, 0.750, 4.000)
ops.node(192, -1.250, 6.000)
ops.node(193, 1.750, 2.000)
ops.node(194, -3.250, 7.000)
ops.node(195, -1.750, 6.500)
ops.node(196, 1.250, 3.500)
ops.node(198, 1.750, 2.500)
ops.node(199, -0.250, 5.500)
ops.node(200, 0.250, 5.000)
ops.node(201, -2.750, 7.000)
ops.node(202, -0.750, 6.000)
ops.node(203, 0.750, 4.500)
ops.node(204, -5.250, 7.500)
ops.node(205, 2.250, 0.000)
ops.node(206, -4.750, 7.500)
ops.node(207, 2.250, 0.500)
ops.node(208, -4.250, 7.500)
ops.node(209, 2.250, 1.000)
ops.node(210, 1.750, 3.000)
ops.node(211, -2.250, 7.000)
ops.node(212, 1.250, 4.000)
ops.node(213, -1.250, 6.500)
ops.node(214, 2.250, 1.500)
ops.node(215, -3.750, 7.500)
ops.node(216, -3.250, 7.500)
ops.node(217, 2.250, 2.000)
ops.node(218, 0.250, 5.500)
ops.node(220, 0.750, 5.000)
ops.node(221, -0.250, 6.000)
ops.node(222, -1.750, 7.000)
ops.node(223, 1.750, 3.500)
ops.node(224, -0.750, 6.500)
ops.node(225, 1.250, 4.500)
ops.node(226, -2.750, 7.500)
ops.node(227, 2.250, 2.500)
ops.node(228, -5.250, 8.000)
ops.node(229, 2.750, 0.000)
ops.node(230, -4.750, 8.000)
ops.node(231, 2.750, 0.500)
ops.node(232, -4.250, 8.000)
ops.node(233, 2.750, 1.000)
ops.node(234, 1.750, 4.000)
ops.node(235, -1.250, 7.000)
ops.node(236, -2.250, 7.500)
ops.node(237, 2.250, 3.000)
ops.node(238, -3.750, 8.000)
ops.node(239, 0.750, 5.500)
ops.node(240, 2.750, 1.500)
ops.node(241, 0.250, 6.000)
ops.node(243, 1.250, 5.000)
ops.node(244, -0.250, 6.500)
ops.node(245, 2.750, 2.000)
ops.node(246, -3.250, 8.000)
ops.node(247, -1.750, 7.500)
ops.node(248, 2.250, 3.500)
ops.node(249, -0.750, 7.000)
ops.node(250, 1.750, 4.500)
ops.node(251, -2.750, 8.000)
ops.node(252, 2.750, 2.500)
ops.node(253, 0.750, 6.000)
ops.node(254, 2.250, 4.000)
ops.node(255, -5.250, 8.500)
ops.node(256, 3.250, 0.000)
ops.node(257, -1.250, 7.500)
ops.node(258, -4.750, 8.500)
ops.node(259, 1.250, 5.500)
ops.node(260, 0.250, 6.500)
ops.node(261, 3.250, 0.500)
ops.node(262, -2.250, 8.000)
ops.node(263, 2.750, 3.000)
ops.node(265, -4.250, 8.500)
ops.node(266, 3.250, 1.000)
ops.node(267, -0.250, 7.000)
ops.node(268, 1.750, 5.000)
ops.node(269, -3.750, 8.500)
ops.node(270, 3.250, 1.500)
ops.node(271, -3.250, 8.500)
ops.node(272, -1.750, 8.000)
ops.node(273, 3.250, 2.000)
ops.node(274, 2.750, 3.500)
ops.node(275, 2.250, 4.500)
ops.node(276, -0.750, 7.500)
ops.node(277, 1.250, 6.000)
ops.node(278, 0.750, 6.500)
ops.node(279, -2.750, 8.500)
ops.node(280, 3.250, 2.500)
ops.node(281, 0.250, 7.000)
ops.node(282, 1.750, 5.500)
ops.node(283, -1.250, 8.000)
ops.node(284, 2.750, 4.000)
ops.node(286, 3.750, 0.000)
ops.node(287, -5.250, 9.000)
ops.node(288, -4.750, 9.000)
ops.node(289, -2.250, 8.500)
ops.node(290, 2.250, 5.000)
ops.node(291, -0.250, 7.500)
ops.node(292, 3.250, 3.000)
ops.node(293, 3.750, 0.500)
ops.node(294, -4.250, 9.000)
ops.node(295, 3.750, 1.000)
ops.node(296, -3.750, 9.000)
ops.node(297, 3.750, 1.500)
ops.node(298, -0.750, 8.000)
ops.node(299, 2.750, 4.500)
ops.node(300, -1.750, 8.500)
ops.node(301, 3.250, 3.500)
ops.node(302, 1.250, 6.500)
ops.node(303, 3.750, 2.000)
ops.node(304, 0.750, 7.000)
ops.node(305, -3.250, 9.000)
ops.node(306, 1.750, 6.000)
ops.node(307, 2.250, 5.500)
ops.node(308, 0.250, 7.500)
ops.node(309, 3.750, 2.500)
ops.node(310, -2.750, 9.000)
ops.node(312, 3.250, 4.000)
ops.node(313, -1.250, 8.500)
ops.node(314, 2.750, 5.000)
ops.node(315, -0.250, 8.000)
ops.node(316, 3.750, 3.000)
ops.node(317, -2.250, 9.000)
ops.node(318, -5.250, 9.500)
ops.node(319, 4.250, 0.000)
ops.node(320, -4.750, 9.500)
ops.node(321, 4.250, 0.500)
ops.node(322, 1.250, 7.000)
ops.node(323, -4.250, 9.500)
ops.node(324, 4.250, 1.000)
ops.node(325, 1.750, 6.500)
ops.node(326, 0.750, 7.500)
ops.node(327, 2.250, 6.000)
ops.node(328, -0.750, 8.500)
ops.node(329, 3.250, 4.500)
ops.node(330, 4.250, 1.500)
ops.node(331, -3.750, 9.500)
ops.node(332, -1.750, 9.000)
ops.node(333, 3.750, 3.500)
ops.node(334, 4.250, 2.000)
ops.node(335, 2.750, 5.500)
ops.node(336, 0.250, 8.000)
ops.node(337, -3.250, 9.500)
ops.node(339, 4.250, 2.500)
ops.node(340, -2.750, 9.500)
ops.node(341, 3.750, 4.000)
ops.node(342, -1.250, 9.000)
ops.node(343, 3.250, 5.000)
ops.node(344, -0.250, 8.500)
ops.node(345, 1.750, 7.000)
ops.node(346, 2.250, 6.500)
ops.node(347, 1.250, 7.500)
ops.node(348, 4.250, 3.000)
ops.node(349, -2.250, 9.500)
ops.node(350, 2.750, 6.000)
ops.node(351, -5.250, 10.000)
ops.node(352, 4.750, 0.000)
ops.node(353, 0.750, 8.000)
ops.node(354, -4.750, 10.000)
ops.node(355, 4.750, 0.500)
ops.node(356, 4.750, 1.000)
ops.node(357, -4.250, 10.000)
ops.node(358, 3.750, 4.500)
ops.node(359, -0.750, 9.000)
ops.node(360, -3.750, 10.000)
ops.node(361, 4.750, 1.500)
ops.node(362, 4.250, 3.500)
ops.node(363, 0.250, 8.500)
ops.node(364, 3.250, 5.500)
ops.node(365, -1.750, 9.500)
ops.node(366, -3.250, 10.000)
ops.node(367, 4.750, 2.000)
ops.node(369, 1.750, 7.500)
ops.node(370, 2.250, 7.000)
ops.node(371, 3.750, 5.000)
ops.node(372, -0.250, 9.000)
ops.node(373, 4.750, 2.500)
ops.node(374, 2.750, 6.500)
ops.node(375, -1.250, 9.500)
ops.node(376, -2.750, 10.000)
ops.node(377, 4.250, 4.000)
ops.node(378, 1.250, 8.000)
ops.node(379, 3.250, 6.000)
ops.node(380, 0.750, 8.500)
ops.node(381, 4.750, 3.000)
ops.node(382, -2.250, 10.000)
ops.node(383, 5.250, 0.000)
ops.node(384, 4.250, 4.500)
ops.node(385, 5.250, 0.500)
ops.node(386, -0.750, 9.500)
ops.node(387, 0.250, 9.000)
ops.node(388, 5.250, 1.000)
ops.node(389, 3.750, 5.500)
ops.node(390, 4.750, 3.500)
ops.node(391, -1.750, 10.000)
ops.node(392, 2.250, 7.500)
ops.node(393, 5.250, 1.500)
ops.node(394, 2.750, 7.000)
ops.node(395, 1.750, 8.000)
ops.node(397, 5.250, 2.000)
ops.node(398, 1.250, 8.500)
ops.node(399, 3.250, 6.500)
ops.node(400, -0.250, 9.500)
ops.node(401, 4.250, 5.000)
ops.node(402, -1.250, 10.000)
ops.node(403, 4.750, 4.000)
ops.node(404, 5.250, 2.500)
ops.node(405, 0.750, 9.000)
ops.node(406, 3.750, 6.000)
ops.node(407, 5.250, 3.000)
ops.node(408, 2.750, 7.500)
ops.node(409, 4.750, 4.500)
ops.node(410, -0.750, 10.000)
ops.node(411, 2.250, 8.000)
ops.node(412, 0.250, 9.500)
ops.node(413, 4.250, 5.500)
ops.node(414, 1.750, 8.500)
ops.node(415, 3.250, 7.000)
ops.node(416, 5.250, 3.500)
ops.node(418, 1.250, 9.000)
ops.node(419, 3.750, 6.500)
ops.node(420, 4.750, 5.000)
ops.node(421, -0.250, 10.000)
ops.node(422, 4.250, 6.000)
ops.node(423, 5.250, 4.000)
ops.node(424, 0.750, 9.500)
ops.node(425, 2.750, 8.000)
ops.node(426, 3.250, 7.500)
ops.node(427, 2.250, 8.500)
ops.node(428, 3.750, 7.000)
ops.node(429, 1.750, 9.000)
ops.node(430, 0.250, 10.000)
ops.node(431, 4.750, 5.500)
ops.node(432, 5.250, 4.500)
ops.node(433, 1.250, 9.500)
ops.node(434, 4.250, 6.500)
ops.node(436, 5.250, 5.000)
ops.node(437, 0.750, 10.000)
ops.node(438, 4.750, 6.000)
ops.node(439, 2.750, 8.500)
ops.node(440, 3.250, 8.000)
ops.node(441, 3.750, 7.500)
ops.node(442, 2.250, 9.000)
ops.node(443, 4.250, 7.000)
ops.node(444, 1.750, 9.500)
ops.node(445, 5.250, 5.500)
ops.node(446, 1.250, 10.000)
ops.node(447, 4.750, 6.500)
ops.node(448, 3.250, 8.500)
ops.node(449, 3.750, 8.000)
ops.node(450, 2.750, 9.000)
ops.node(451, 5.250, 6.000)
ops.node(452, 4.250, 7.500)
ops.node(453, 2.250, 9.500)
ops.node(454, 4.750, 7.000)
ops.node(455, 1.750, 10.000)
ops.node(456, 5.250, 6.500)
ops.node(457, 3.750, 8.500)
ops.node(458, 3.250, 9.000)
ops.node(459, 4.250, 8.000)
ops.node(460, 2.750, 9.500)
ops.node(461, 2.250, 10.000)
ops.node(462, 4.750, 7.500)
ops.node(463, 5.250, 7.000)
ops.node(464, 3.750, 9.000)
ops.node(465, 4.250, 8.500)
ops.node(466, 3.250, 9.500)
ops.node(467, 4.750, 8.000)
ops.node(468, 2.750, 10.000)
ops.node(469, 5.250, 7.500)
ops.node(470, 4.250, 9.000)
ops.node(471, 3.750, 9.500)
ops.node(472, 4.750, 8.500)
ops.node(473, 3.250, 10.000)
ops.node(474, 5.250, 8.000)
ops.node(475, 4.250, 9.500)
ops.node(476, 3.750, 10.000)
ops.node(477, 4.750, 9.000)
ops.node(478, 5.250, 8.500)
ops.node(479, 4.750, 9.500)
ops.node(480, 4.250, 10.000)
ops.node(481, 5.250, 9.000)
ops.node(482, 4.750, 10.000)
ops.node(483, 5.250, 9.500)
ops.node(484, 5.250, 10.000)
print('"Finished', 'creating', 'all', '-ndf', 2, 'soil', 'nodes..."')

# define fixities for soil nodes
ops.fix(1, 1, 1)
ops.fix(2, 1, 0)
ops.fix(3, 0, 1)
ops.fix(5, 0, 1)
ops.fix(6, 1, 0)
ops.fix(10, 1, 0)
ops.fix(11, 0, 1)
ops.fix(16, 0, 1)
ops.fix(17, 1, 0)
ops.fix(23, 1, 0)
ops.fix(24, 0, 1)
ops.fix(34, 1, 0)
ops.fix(35, 0, 1)
ops.fix(44, 1, 0)
ops.fix(45, 0, 1)
ops.fix(57, 1, 0)
ops.fix(58, 0, 1)
ops.fix(72, 0, 1)
ops.fix(73, 1, 0)
ops.fix(87, 1, 0)
ops.fix(88, 0, 1)
ops.fix(109, 0, 1)
ops.fix(110, 1, 0)
ops.fix(129, 1, 0)
ops.fix(130, 0, 1)
ops.fix(152, 0, 1)
ops.fix(154, 1, 0)
ops.fix(177, 1, 0)
ops.fix(178, 0, 1)
ops.fix(204, 1, 0)
ops.fix(205, 0, 1)
ops.fix(228, 1, 0)
ops.fix(229, 0, 1)
ops.fix(255, 1, 0)
ops.fix(256, 0, 1)
ops.fix(286, 0, 1)
ops.fix(287, 1, 0)
ops.fix(318, 1, 0)
ops.fix(319, 0, 1)
ops.fix(351, 1, 0)
ops.fix(352, 0, 1)
ops.fix(383, 1, 1)
ops.fix(385, 1, 0)
ops.fix(388, 1, 0)
ops.fix(393, 1, 0)
ops.fix(397, 1, 0)
ops.fix(404, 1, 0)
ops.fix(407, 1, 0)
ops.fix(416, 1, 0)
ops.fix(423, 1, 0)
ops.fix(432, 1, 0)
ops.fix(436, 1, 0)
ops.fix(445, 1, 0)
ops.fix(451, 1, 0)
ops.fix(456, 1, 0)
ops.fix(463, 1, 0)
ops.fix(469, 1, 0)
ops.fix(474, 1, 0)
ops.fix(478, 1, 0)
ops.fix(481, 1, 0)
ops.fix(483, 1, 0)
ops.fix(484, 1, 0)
print('"Finished', 'creating', 'all', '-ndf', 2, 'boundary', 'conditions..."')

# --------------------------------------------------------------------------
#  3. CREATE LAGRANGE MULTIPLIER NODES FOR BEAM CONTACT ELEMENTS
# --------------------------------------------------------------------------

for k in range(1, 43):
    ops.node(1000 + k, 0.0, 0.0)
print('"Finished', 'creating', 'all', '-ndf', 2, 'nodes..."')

# --------------------------------------------------------------------------
#  4. CREATE SOIL MATERIALS
# ---------------------------------------------------------------------------

# define pressure depended material for soil
ops.nDMaterial('PressureDependMultiYield02', 5, 2, 1.8, 9.6e3, 2.7e4, 36, 0.1,
               101.0, 0.0, 26, 0.067, 0.23, 0.06, 0.27, 20, 5.0, 3.0, 1.0,
               0.0, 0.77, 0.9, 0.02, 0.7, 101.0)
# element thickness
thick1 = 1.0
# body force in x-direction
xWgt1 = 0.0
# body force in y-direction
yWgt1 = -9.81 * 1.8

# create wrapper material for initial state analysis
ops.nDMaterial('InitialStateAnalysisWrapper', 1, 5, 2)

print('"Finished', 'creating', 'all', 'soil', 'materials..."')

# ---------------------------------------------------------------------------
#  5. CREATE SOIL ELEMENTS
# ---------------------------------------------------------------------------

ops.element('quad', 1, 109, 130, 131, 112, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 2, 130, 152, 157, 131, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 3, 152, 178, 180, 157, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 4, 178, 205, 207, 180, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 5, 205, 229, 231, 207, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 6, 229, 256, 261, 231, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 7, 256, 286, 293, 261, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 8, 286, 319, 321, 293, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 9, 319, 352, 355, 321, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 10, 352, 383, 385, 355, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 11, 112, 131, 138, 116, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 12, 131, 157, 161, 138, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 13, 157, 180, 181, 161, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 14, 180, 207, 209, 181, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 15, 207, 231, 233, 209, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 16, 231, 261, 266, 233, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 17, 261, 293, 295, 266, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 18, 293, 321, 324, 295, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 19, 321, 355, 356, 324, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 20, 355, 385, 388, 356, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 21, 116, 138, 143, 119, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 22, 138, 161, 162, 143, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 23, 161, 181, 187, 162, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 24, 181, 209, 214, 187, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 25, 209, 233, 240, 214, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 26, 233, 266, 270, 240, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 27, 266, 295, 297, 270, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 28, 295, 324, 330, 297, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 29, 324, 356, 361, 330, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 30, 356, 388, 393, 361, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 31, 119, 143, 146, 126, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 32, 143, 162, 170, 146, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 33, 162, 187, 193, 170, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 34, 187, 214, 217, 193, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 35, 214, 240, 245, 217, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 36, 240, 270, 273, 245, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 37, 270, 297, 303, 273, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 38, 297, 330, 334, 303, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 39, 330, 361, 367, 334, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 40, 361, 393, 397, 367, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 41, 126, 146, 153, 135, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 42, 146, 170, 176, 153, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 43, 170, 193, 198, 176, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 44, 193, 217, 227, 198, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 45, 217, 245, 252, 227, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 46, 245, 273, 280, 252, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 47, 273, 303, 309, 280, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 48, 303, 334, 339, 309, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 49, 334, 367, 373, 339, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 50, 367, 397, 404, 373, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 51, 135, 153, 164, 144, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 52, 153, 176, 189, 164, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 53, 176, 198, 210, 189, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 54, 198, 227, 237, 210, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 55, 227, 252, 263, 237, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 56, 252, 280, 292, 263, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 57, 280, 309, 316, 292, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 58, 309, 339, 348, 316, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 59, 339, 373, 381, 348, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 60, 373, 404, 407, 381, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 61, 144, 164, 173, 158, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 62, 164, 189, 196, 173, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 63, 189, 210, 223, 196, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 64, 210, 237, 248, 223, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 65, 237, 263, 274, 248, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 66, 263, 292, 301, 274, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 67, 292, 316, 333, 301, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 68, 316, 348, 362, 333, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 69, 348, 381, 390, 362, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 70, 381, 407, 416, 390, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 71, 158, 173, 191, 171, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 72, 173, 196, 212, 191, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 73, 196, 223, 234, 212, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 74, 223, 248, 254, 234, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 75, 248, 274, 284, 254, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 76, 274, 301, 312, 284, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 77, 301, 333, 341, 312, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 78, 333, 362, 377, 341, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 79, 362, 390, 403, 377, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 80, 390, 416, 423, 403, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 81, 171, 191, 203, 185, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 82, 191, 212, 225, 203, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 83, 212, 234, 250, 225, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 84, 234, 254, 275, 250, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 85, 254, 284, 299, 275, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 86, 284, 312, 329, 299, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 87, 312, 341, 358, 329, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 88, 341, 377, 384, 358, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 89, 377, 403, 409, 384, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 90, 403, 423, 432, 409, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 91, 185, 203, 220, 200, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 92, 203, 225, 243, 220, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 93, 225, 250, 268, 243, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 94, 250, 275, 290, 268, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 95, 275, 299, 314, 290, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 96, 299, 329, 343, 314, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 97, 329, 358, 371, 343, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 98, 358, 384, 401, 371, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 99, 384, 409, 420, 401, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 100, 409, 432, 436, 420, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 101, 200, 220, 239, 218, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 102, 220, 243, 259, 239, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 103, 243, 268, 282, 259, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 104, 268, 290, 307, 282, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 105, 290, 314, 335, 307, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 106, 314, 343, 364, 335, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 107, 343, 371, 389, 364, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 108, 371, 401, 413, 389, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 109, 401, 420, 431, 413, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 110, 420, 436, 445, 431, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 111, 218, 239, 253, 241, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 112, 239, 259, 277, 253, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 113, 259, 282, 306, 277, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 114, 282, 307, 327, 306, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 115, 307, 335, 350, 327, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 116, 335, 364, 379, 350, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 117, 364, 389, 406, 379, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 118, 389, 413, 422, 406, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 119, 413, 431, 438, 422, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 120, 431, 445, 451, 438, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 121, 241, 253, 278, 260, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 122, 253, 277, 302, 278, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 123, 277, 306, 325, 302, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 124, 306, 327, 346, 325, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 125, 327, 350, 374, 346, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 126, 350, 379, 399, 374, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 127, 379, 406, 419, 399, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 128, 406, 422, 434, 419, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 129, 422, 438, 447, 434, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 130, 438, 451, 456, 447, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 131, 260, 278, 304, 281, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 132, 278, 302, 322, 304, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 133, 302, 325, 345, 322, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 134, 325, 346, 370, 345, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 135, 346, 374, 394, 370, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 136, 374, 399, 415, 394, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 137, 399, 419, 428, 415, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 138, 419, 434, 443, 428, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 139, 434, 447, 454, 443, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 140, 447, 456, 463, 454, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 141, 281, 304, 326, 308, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 142, 304, 322, 347, 326, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 143, 322, 345, 369, 347, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 144, 345, 370, 392, 369, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 145, 370, 394, 408, 392, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 146, 394, 415, 426, 408, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 147, 415, 428, 441, 426, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 148, 428, 443, 452, 441, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 149, 443, 454, 462, 452, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 150, 454, 463, 469, 462, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 151, 308, 326, 353, 336, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 152, 326, 347, 378, 353, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 153, 347, 369, 395, 378, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 154, 369, 392, 411, 395, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 155, 392, 408, 425, 411, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 156, 408, 426, 440, 425, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 157, 426, 441, 449, 440, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 158, 441, 452, 459, 449, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 159, 452, 462, 467, 459, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 160, 462, 469, 474, 467, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 161, 336, 353, 380, 363, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 162, 353, 378, 398, 380, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 163, 378, 395, 414, 398, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 164, 395, 411, 427, 414, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 165, 411, 425, 439, 427, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 166, 425, 440, 448, 439, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 167, 440, 449, 457, 448, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 168, 449, 459, 465, 457, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 169, 459, 467, 472, 465, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 170, 467, 474, 478, 472, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 171, 363, 380, 405, 387, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 172, 380, 398, 418, 405, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 173, 398, 414, 429, 418, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 174, 414, 427, 442, 429, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 175, 427, 439, 450, 442, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 176, 439, 448, 458, 450, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 177, 448, 457, 464, 458, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 178, 457, 465, 470, 464, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 179, 465, 472, 477, 470, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 180, 472, 478, 481, 477, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 181, 387, 405, 424, 412, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 182, 405, 418, 433, 424, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 183, 418, 429, 444, 433, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 184, 429, 442, 453, 444, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 185, 442, 450, 460, 453, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 186, 450, 458, 466, 460, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 187, 458, 464, 471, 466, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 188, 464, 470, 475, 471, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 189, 470, 477, 479, 475, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 190, 477, 481, 483, 479, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 191, 412, 424, 437, 430, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 192, 424, 433, 446, 437, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 193, 433, 444, 455, 446, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 194, 444, 453, 461, 455, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 195, 453, 460, 468, 461, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 196, 460, 466, 473, 468, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 197, 466, 471, 476, 473, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 198, 471, 475, 480, 476, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 199, 475, 479, 482, 480, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 200, 479, 483, 484, 482, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 201, 88, 92, 75, 72, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 202, 92, 93, 79, 75, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 203, 93, 98, 83, 79, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 204, 98, 105, 84, 83, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 205, 105, 115, 95, 84, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 206, 115, 125, 107, 95, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 207, 125, 139, 122, 107, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 208, 139, 150, 134, 122, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 209, 150, 166, 148, 134, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 210, 166, 182, 167, 148, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 211, 182, 199, 186, 167, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 212, 199, 221, 202, 186, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 213, 221, 244, 224, 202, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 214, 244, 267, 249, 224, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 215, 267, 291, 276, 249, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 216, 291, 315, 298, 276, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 217, 315, 344, 328, 298, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 218, 344, 372, 359, 328, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 219, 372, 400, 386, 359, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 220, 400, 421, 410, 386, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 221, 72, 75, 59, 58, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 222, 75, 79, 64, 59, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 223, 79, 83, 67, 64, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 224, 83, 84, 70, 67, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 225, 84, 95, 80, 70, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 226, 95, 107, 89, 80, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 227, 107, 122, 103, 89, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 228, 122, 134, 118, 103, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 229, 134, 148, 132, 118, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 230, 148, 167, 149, 132, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 231, 167, 186, 172, 149, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 232, 186, 202, 192, 172, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 233, 202, 224, 213, 192, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 234, 224, 249, 235, 213, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 235, 249, 276, 257, 235, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 236, 276, 298, 283, 257, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 237, 298, 328, 313, 283, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 238, 328, 359, 342, 313, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 239, 359, 386, 375, 342, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 240, 386, 410, 402, 375, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 241, 58, 59, 48, 45, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 242, 59, 64, 51, 48, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 243, 64, 67, 54, 51, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 244, 67, 70, 61, 54, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 245, 70, 80, 68, 61, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 246, 80, 89, 77, 68, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 247, 89, 103, 86, 77, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 248, 103, 118, 102, 86, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 249, 118, 132, 121, 102, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 250, 132, 149, 140, 121, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 251, 149, 172, 159, 140, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 252, 172, 192, 174, 159, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 253, 192, 213, 195, 174, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 254, 213, 235, 222, 195, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 255, 235, 257, 247, 222, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 256, 257, 283, 272, 247, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 257, 283, 313, 300, 272, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 258, 313, 342, 332, 300, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 259, 342, 375, 365, 332, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 260, 375, 402, 391, 365, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 261, 45, 48, 37, 35, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 262, 48, 51, 39, 37, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 263, 51, 54, 43, 39, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 264, 54, 61, 49, 43, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 265, 61, 68, 55, 49, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 266, 68, 77, 65, 55, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 267, 77, 86, 78, 65, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 268, 86, 102, 90, 78, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 269, 102, 121, 108, 90, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 270, 121, 140, 124, 108, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 271, 140, 159, 145, 124, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 272, 159, 174, 165, 145, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 273, 174, 195, 188, 165, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 274, 195, 222, 211, 188, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 275, 222, 247, 236, 211, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 276, 247, 272, 262, 236, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 277, 272, 300, 289, 262, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 278, 300, 332, 317, 289, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 279, 332, 365, 349, 317, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 280, 365, 391, 382, 349, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 281, 35, 37, 28, 24, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 282, 37, 39, 30, 28, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 283, 39, 43, 33, 30, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 284, 43, 49, 41, 33, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 285, 49, 55, 46, 41, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 286, 55, 65, 56, 46, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 287, 65, 78, 69, 56, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 288, 78, 90, 81, 69, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 289, 90, 108, 96, 81, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 290, 108, 124, 114, 96, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 291, 124, 145, 136, 114, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 292, 145, 165, 155, 136, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 293, 165, 188, 175, 155, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 294, 188, 211, 201, 175, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 295, 211, 236, 226, 201, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 296, 236, 262, 251, 226, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 297, 262, 289, 279, 251, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 298, 289, 317, 310, 279, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 299, 317, 349, 340, 310, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 300, 349, 382, 376, 340, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 301, 24, 28, 19, 16, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 302, 28, 30, 21, 19, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 303, 30, 33, 25, 21, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 304, 33, 41, 31, 25, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 305, 41, 46, 40, 31, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 306, 46, 56, 50, 40, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 307, 56, 69, 62, 50, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 308, 69, 81, 71, 62, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 309, 81, 96, 85, 71, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 310, 96, 114, 104, 85, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 311, 114, 136, 127, 104, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 312, 136, 155, 147, 127, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 313, 155, 175, 169, 147, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 314, 175, 201, 194, 169, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 315, 201, 226, 216, 194, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 316, 226, 251, 246, 216, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 317, 251, 279, 271, 246, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 318, 279, 310, 305, 271, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 319, 310, 340, 337, 305, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 320, 340, 376, 366, 337, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 321, 16, 19, 13, 11, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 322, 19, 21, 14, 13, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 323, 21, 25, 20, 14, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 324, 25, 31, 26, 20, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 325, 31, 40, 32, 26, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 326, 40, 50, 42, 32, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 327, 50, 62, 53, 42, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 328, 62, 71, 66, 53, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 329, 71, 85, 82, 66, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 330, 85, 104, 97, 82, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 331, 104, 127, 120, 97, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 332, 127, 147, 142, 120, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 333, 147, 169, 163, 142, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 334, 169, 194, 190, 163, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 335, 194, 216, 215, 190, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 336, 216, 246, 238, 215, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 337, 246, 271, 269, 238, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 338, 271, 305, 296, 269, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 339, 305, 337, 331, 296, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 340, 337, 366, 360, 331, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 341, 11, 13, 8, 5, thick1, 'PlaneStrain', 1, 0.0, 0.0,
            xWgt1, yWgt1)
ops.element('quad', 342, 13, 14, 9, 8, thick1, 'PlaneStrain', 1, 0.0, 0.0,
            xWgt1, yWgt1)
ops.element('quad', 343, 14, 20, 15, 9, thick1, 'PlaneStrain', 1, 0.0, 0.0,
            xWgt1, yWgt1)
ops.element('quad', 344, 20, 26, 22, 15, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 345, 26, 32, 29, 22, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 346, 32, 42, 38, 29, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 347, 42, 53, 52, 38, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 348, 53, 66, 63, 52, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 349, 66, 82, 76, 63, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 350, 82, 97, 94, 76, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 351, 97, 120, 117, 94, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 352, 120, 142, 137, 117, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 353, 142, 163, 160, 137, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 354, 163, 190, 183, 160, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 355, 190, 215, 208, 183, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 356, 215, 238, 232, 208, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 357, 238, 269, 265, 232, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 358, 269, 296, 294, 265, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 359, 296, 331, 323, 294, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 360, 331, 360, 357, 323, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 361, 5, 8, 4, 3, thick1, 'PlaneStrain', 1, 0.0, 0.0,
            xWgt1, yWgt1)
ops.element('quad', 362, 8, 9, 7, 4, thick1, 'PlaneStrain', 1, 0.0, 0.0,
            xWgt1, yWgt1)
ops.element('quad', 363, 9, 15, 12, 7, thick1, 'PlaneStrain', 1, 0.0, 0.0,
            xWgt1, yWgt1)
ops.element('quad', 364, 15, 22, 18, 12, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 365, 22, 29, 27, 18, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 366, 29, 38, 36, 27, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 367, 38, 52, 47, 36, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 368, 52, 63, 60, 47, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 369, 63, 76, 74, 60, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 370, 76, 94, 91, 74, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 371, 94, 117, 111, 91, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 372, 117, 137, 133, 111, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 373, 137, 160, 156, 133, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 374, 160, 183, 179, 156, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 375, 183, 208, 206, 179, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 376, 208, 232, 230, 206, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 377, 232, 265, 258, 230, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 378, 265, 294, 288, 258, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 379, 294, 323, 320, 288, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 380, 323, 357, 354, 320, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 381, 3, 4, 2, 1, thick1, 'PlaneStrain', 1, 0.0, 0.0,
            xWgt1, yWgt1)
ops.element('quad', 382, 4, 7, 6, 2, thick1, 'PlaneStrain', 1, 0.0, 0.0,
            xWgt1, yWgt1)
ops.element('quad', 383, 7, 12, 10, 6, thick1, 'PlaneStrain', 1, 0.0, 0.0,
            xWgt1, yWgt1)
ops.element('quad', 384, 12, 18, 17, 10, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 385, 18, 27, 23, 17, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 386, 27, 36, 34, 23, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 387, 36, 47, 44, 34, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 388, 47, 60, 57, 44, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 389, 60, 74, 73, 57, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 390, 74, 91, 87, 73, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 391, 91, 111, 110, 87, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 392, 111, 133, 129, 110, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 393, 133, 156, 154, 129, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 394, 156, 179, 177, 154, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 395, 179, 206, 204, 177, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 396, 206, 230, 228, 204, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 397, 230, 258, 255, 228, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 398, 258, 288, 287, 255, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 399, 288, 320, 318, 287, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
ops.element('quad', 400, 320, 354, 351, 318, thick1, 'PlaneStrain', 1, 0.0,
            0.0, xWgt1, yWgt1)
print('"Finished', 'creating', 'all', 'soil', 'elements..."')

# ---------------------------------------------------------------------------
#  6. CREATE BEAM NODES AND FIXITIES
# ---------------------------------------------------------------------------
ops.model('BasicBuilder', '-ndm', 2, '-ndf', 3)

# define beam nodes
ops.node(99, 0.000, 0.250)
ops.node(100, 0.000, -0.250)
ops.node(101, 0.000, 0.750)
ops.node(106, 0.000, 1.250)
ops.node(113, 0.000, 1.750)
ops.node(123, 0.000, 2.250)
ops.node(128, 0.000, 2.750)
ops.node(141, 0.000, 3.250)
ops.node(151, 0.000, 3.750)
ops.node(168, 0.000, 4.250)
ops.node(184, 0.000, 4.750)
ops.node(197, 0.000, 5.250)
ops.node(219, 0.000, 5.750)
ops.node(242, 0.000, 6.250)
ops.node(264, 0.000, 6.750)
ops.node(285, 0.000, 7.250)
ops.node(311, 0.000, 7.750)
ops.node(338, 0.000, 8.250)
ops.node(368, 0.000, 8.750)
ops.node(396, 0.000, 9.250)
ops.node(417, 0.000, 9.750)
ops.node(435, 0.000, 10.250)
print('"Finished', 'creating', 'all', '-ndf', 3, 'beam', 'nodes..."')

# fix the base node of the sheetpile in the vertial direction
ops.fix(100, 0, 1, 0)
print('"Finished', 'creating', 'all', '-ndf', 3, 'boundary', 'conditions..."')

# --------------------------------------------------------------------------
#  7. CREATE BEAM MATERIALS
# --------------------------------------------------------------------------

# beam properties
thick = 0.5
area = 0.5
I = 9.75e-4
beamE = 200000000
numIntPts = 3
transTag = 1
secTag = 1

# geometric transformation
ops.geomTransf('Linear', 1)

# beam section
ops.section('Elastic', secTag, beamE, area, I)
print('"Finished', 'creating', 'all', 'beam', 'materials..."')

# --------------------------------------------------------------------------
#  8. CREATE BEAM ELEMENTS
# ---------------------------------------------------------------------------

ops.beamIntegration('Legendre', 401, secTag, numIntPts)
ops.element('dispBeamColumn', 401, 100, 99, transTag, 401)
ops.beamIntegration('Legendre', 402, secTag, numIntPts)
ops.element('dispBeamColumn', 402, 99, 101, transTag, 402)
ops.beamIntegration('Legendre', 403, secTag, numIntPts)
ops.element('dispBeamColumn', 403, 101, 106, transTag, 403)
ops.beamIntegration('Legendre', 404, secTag, numIntPts)
ops.element('dispBeamColumn', 404, 106, 113, transTag, 404)
ops.beamIntegration('Legendre', 405, secTag, numIntPts)
ops.element('dispBeamColumn', 405, 113, 123, transTag, 405)
ops.beamIntegration('Legendre', 406, secTag, numIntPts)
ops.element('dispBeamColumn', 406, 123, 128, transTag, 406)
ops.beamIntegration('Legendre', 407, secTag, numIntPts)
ops.element('dispBeamColumn', 407, 128, 141, transTag, 407)
ops.beamIntegration('Legendre', 408, secTag, numIntPts)
ops.element('dispBeamColumn', 408, 141, 151, transTag, 408)
ops.beamIntegration('Legendre', 409, secTag, numIntPts)
ops.element('dispBeamColumn', 409, 151, 168, transTag, 409)
ops.beamIntegration('Legendre', 410, secTag, numIntPts)
ops.element('dispBeamColumn', 410, 168, 184, transTag, 410)
ops.beamIntegration('Legendre', 411, secTag, numIntPts)
ops.element('dispBeamColumn', 411, 184, 197, transTag, 411)
ops.beamIntegration('Legendre', 412, secTag, numIntPts)
ops.element('dispBeamColumn', 412, 197, 219, transTag, 412)
ops.beamIntegration('Legendre', 413, secTag, numIntPts)
ops.element('dispBeamColumn', 413, 219, 242, transTag, 413)
ops.beamIntegration('Legendre', 414, secTag, numIntPts)
ops.element('dispBeamColumn', 414, 242, 264, transTag, 414)
ops.beamIntegration('Legendre', 415, secTag, numIntPts)
ops.element('dispBeamColumn', 415, 264, 285, transTag, 415)
ops.beamIntegration('Legendre', 416, secTag, numIntPts)
ops.element('dispBeamColumn', 416, 285, 311, transTag, 416)
ops.beamIntegration('Legendre', 417, secTag, numIntPts)
ops.element('dispBeamColumn', 417, 311, 338, transTag, 417)
ops.beamIntegration('Legendre', 418, secTag, numIntPts)
ops.element('dispBeamColumn', 418, 338, 368, transTag, 418)
ops.beamIntegration('Legendre', 419, secTag, numIntPts)
ops.element('dispBeamColumn', 419, 368, 396, transTag, 419)
ops.beamIntegration('Legendre', 420, secTag, numIntPts)
ops.element('dispBeamColumn', 420, 396, 417, transTag, 420)
ops.beamIntegration('Legendre', 421, secTag, numIntPts)
ops.element('dispBeamColumn', 421, 417, 435, transTag, 421)
print('"Finished', 'creating', 'all', 'beam', 'elements..."')

# --------------------------------------------------------------------------
#  9. CREATE CONTACT MATERIAL FOR BEAM CONTACT ELEMENTS
# --------------------------------------------------------------------------

# two-dimensional contact material
ops.nDMaterial('ContactMaterial2D', 2, 0.1, 1000.0, 0.0, 0.0)

print('"Finished', 'creating', 'all', 'contact', 'materials..."')

# ---------------------------------------------------------------------------
#  10. CREATE BEAM CONTACT ELEMENTS
# ---------------------------------------------------------------------------

# set gap and force tolerances for beam contact elements
gapTol = 1.0e-10
forceTol = 1.0e-10

# define beam contact elements
ops.element('BeamContact2D', 1001, 100, 99, 88, 1001, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1002, 100, 99, 109, 1002, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1003, 99, 101, 92, 1003, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1004, 99, 101, 112, 1004, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1005, 101, 106, 93, 1005, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1006, 101, 106, 116, 1006, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1007, 106, 113, 98, 1007, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1008, 106, 113, 119, 1008, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1009, 113, 123, 105, 1009, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1010, 113, 123, 126, 1010, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1011, 123, 128, 115, 1011, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1012, 123, 128, 135, 1012, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1013, 128, 141, 125, 1013, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1014, 128, 141, 144, 1014, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1015, 141, 151, 139, 1015, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1016, 141, 151, 158, 1016, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1017, 151, 168, 150, 1017, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1018, 151, 168, 171, 1018, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1019, 168, 184, 166, 1019, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1020, 168, 184, 185, 1020, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1021, 184, 197, 182, 1021, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1022, 184, 197, 200, 1022, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1023, 197, 219, 199, 1023, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1024, 197, 219, 218, 1024, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1025, 219, 242, 221, 1025, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1026, 219, 242, 241, 1026, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1027, 242, 264, 244, 1027, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1028, 242, 264, 260, 1028, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1029, 264, 285, 267, 1029, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1030, 264, 285, 281, 1030, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1031, 285, 311, 291, 1031, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1032, 285, 311, 308, 1032, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1033, 311, 338, 315, 1033, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1034, 311, 338, 336, 1034, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1035, 338, 368, 344, 1035, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1036, 338, 368, 363, 1036, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1037, 368, 396, 372, 1037, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1038, 368, 396, 387, 1038, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1039, 396, 417, 400, 1039, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1040, 396, 417, 412, 1040, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1041, 417, 435, 421, 1041, 2, thick, gapTol,
            forceTol)
ops.element('BeamContact2D', 1042, 417, 435, 430, 1042, 2, thick, gapTol,
            forceTol)

print('"Finished', 'creating', 'all', 'beam-contact', 'elements..."')

ops.printGID('model.msh')
# ---------------------------------------------------------------------------
#  12. GRAVITY ANALYSIS (w/ INITIAL STATE ANALYSIS TO RESET DISPLACEMENTS)
# ---------------------------------------------------------------------------

# define analysis parameters for gravity phase
ops.constraints('Transformation')
ops.test('NormDispIncr', 1e-5, 15, 1)
ops.algorithm('Newton')
ops.numberer('RCM')
ops.system('SparseGeneral')
ops.integrator('LoadControl', 1)
ops.analysis('Static')

# turn on initial state analysis feature
ops.InitialStateAnalysis('on')

# ensure soil material intially considers linear elastic behavior
ops.updateMaterialStage('-material', 1, '-stage', 0)

# set contact elements to be frictionless for gravity analysis
ops.setParameter('-val', 0, '-eleRange', 1001, 1042, 'friction')

ops.analyze(4)

# update soil material to consider elastoplastic behavior and analyze a few more steps
ops.updateMaterialStage('-material', 1, '-stage', 1)

ops.analyze(4)

# designate end of initial state analysis (zeros displacements, keeps state variables)
ops.InitialStateAnalysis('off')

# turn on frictional behavior for beam contact elements
ops.setParameter('-val', 1, '-eleRange', 1001, 1042, 'friction')

# ---------------------------------------------------------------------------
#  14. REMOVE ELEMENTS TO SIMULATE EXCAVATION
# ---------------------------------------------------------------------------


# recorder
node_list = ops.getNodeTags()
ops.recorder('Node', '-file', 'disp.txt', '-time', '-node', *node_list,
             '-dof', 1, 2, 'disp')

# load
ops.timeSeries('Constant', 1)
ops.pattern('Plain', 1, 1)
ops.load(435, 10, 0, 0)


# define analysis parameters for excavation phase
ops.constraints('Transformation')
ops.test('NormDispIncr', 1e-4, 60, 1)
ops.algorithm('KrylovNewton')
ops.numberer('RCM')
# ops.system('SparseGeneral')
ops.system('BandSPD')
ops.integrator('LoadControl', 0.1)
ops.analysis('Static')

# remove objects associated with lift 1-----------------------------------
# soil elements
for k in range(1, 11):
    ops.remove('element', 190 + k)
# contact element
ops.remove('element', 1042)
# lagrange multiplier node
ops.remove('node', 1042)
# soil nodes
ops.remove('node', 430)
ops.remove('node', 437)
ops.remove('node', 446)
ops.remove('node', 455)
ops.remove('node', 461)
ops.remove('node', 468)
ops.remove('node', 473)
ops.remove('node', 476)
ops.remove('node', 480)
ops.remove('node', 482)
ops.remove('node', 484)

# run analysis after object removal
ops.analyze(4)

# remove objects associated with lift 2-----------------------------------
# # soil elements
for k in range(1, 11):
    ops.remove('element', 180 + k)
# contact element
ops.remove('element', 1040)
# lagrange multiplier node
ops.remove('node', 1040)
# soil nodes
ops.remove('node', 412)
ops.remove('node', 424)
ops.remove('node', 433)
ops.remove('node', 444)
ops.remove('node', 453)
ops.remove('node', 460)
ops.remove('node', 466)
ops.remove('node', 471)
ops.remove('node', 475)
ops.remove('node', 479)
ops.remove('node', 483)

# run analysis after object removal
ops.analyze(4)

# remove objects associated with lift 3-----------------------------------

# soil elements
for k in range(1, 11):
    ops.remove('element', 170 + k)

# contact element
ops.remove('element', 1038)
# lagrange multiplier node
ops.remove('node', 1038)
# soil nodes
ops.remove('node', 387)
ops.remove('node', 405)
ops.remove('node', 418)
ops.remove('node', 429)
ops.remove('node', 442)
ops.remove('node', 450)
ops.remove('node', 458)
ops.remove('node', 464)
ops.remove('node', 470)
ops.remove('node', 477)
ops.remove('node', 481)

# run analysis after object removal
ops.analyze(4)

# remove objects associated with lift 4-----------------------------------

# # soil elements
for k in range(1, 11):
    ops.remove('element', 160 + k)
# contact element
ops.remove('element', 1036)
# lagrange multiplier node
ops.remove('node', 1036)
# soil nodes
ops.remove('node', 363)
ops.remove('node', 380)
ops.remove('node', 398)
ops.remove('node', 414)
ops.remove('node', 427)
ops.remove('node', 439)
ops.remove('node', 448)
ops.remove('node', 457)
ops.remove('node', 465)
ops.remove('node', 472)
ops.remove('node', 478)

# run analysis after object removal
ops.analyze(4)

# remove objects associated with lift 5-----------------------------------
# soil elements
for k in range(1, 11):
    ops.remove('element', 150 + k)
# contact element
ops.remove('element', 1034)
# lagrange multiplier node
ops.remove('node', 1034)
# soil nodes
ops.remove('node', 336)
ops.remove('node', 353)
ops.remove('node', 378)
ops.remove('node', 395)
ops.remove('node', 411)
ops.remove('node', 425)
ops.remove('node', 440)
ops.remove('node', 449)
ops.remove('node', 459)
ops.remove('node', 467)
ops.remove('node', 474)

# run analysis after object removal
ops.analyze(4)

# # remove objects associated with lift 6-----------------------------------
# # soil elements
for k in range(1, 11):
    ops.remove('element', 140 + k)
# contact element
ops.remove('element', 1032)
# lagrange multiplier node
ops.remove('node', 1032)
# soil nodes
ops.remove('node', 308)
ops.remove('node', 326)
ops.remove('node', 347)
ops.remove('node', 369)
ops.remove('node', 392)
ops.remove('node', 408)
ops.remove('node', 426)
ops.remove('node', 441)
ops.remove('node', 452)
ops.remove('node', 462)
ops.remove('node', 469)

# run analysis after object removal
ops.analyze(4)

# remove objects associated with lift 7-----------------------------------
# soil elements
for k in range(1, 11):
    ops.remove('element', 130 + k)
# contact element
ops.remove('element', 1030)
# lagrange multiplier node
ops.remove('node', 1030)
# soil nodes
ops.remove('node', 281)
ops.remove('node', 304)
ops.remove('node', 322)
ops.remove('node', 345)
ops.remove('node', 370)
ops.remove('node', 394)
ops.remove('node', 415)
ops.remove('node', 428)
ops.remove('node', 443)
ops.remove('node', 454)
ops.remove('node', 463)

# run analysis after object removal
ops.analyze(4)

# remove objects associated with lift 8-----------------------------------
# soil elements
for k in range(1, 11):
    ops.remove('element', 120 + k)
# contact element
ops.remove('element', 1028)
# lagrange multiplier node
ops.remove('node', 1028)
# soil nodes
ops.remove('node', 260)
ops.remove('node', 278)
ops.remove('node', 302)
ops.remove('node', 325)
ops.remove('node', 346)
ops.remove('node', 374)
ops.remove('node', 399)
ops.remove('node', 419)
ops.remove('node', 434)
ops.remove('node', 447)
ops.remove('node', 456)

# run analysis after object removal
ops.analyze(4)

# remove objects associated with lift 9-----------------------------------
# soil elements
for k in range(1, 11):
    ops.remove('element', 110 + k)
# contact element
ops.remove('element', 1026)
# lagrange multiplier node
ops.remove('node', 1026)
# soil nodes
ops.remove('node', 241)
ops.remove('node', 253)
ops.remove('node', 277)
ops.remove('node', 306)
ops.remove('node', 327)
ops.remove('node', 350)
ops.remove('node', 379)
ops.remove('node', 406)
ops.remove('node', 422)
ops.remove('node', 438)
ops.remove('node', 451)

# run analysis after object removal
ops.analyze(4)

# remove objects associated with lift 10----------------------------------
# soil elements
for k in range(1, 11):
    ops.remove('element', 100 + k)
# contact element
ops.remove('element', 1024)
# lagrange multiplier node
ops.remove('node', 1024)
# soil nodes
ops.remove('node', 218)
ops.remove('node', 239)
ops.remove('node', 259)
ops.remove('node', 282)
ops.remove('node', 307)
ops.remove('node', 335)
ops.remove('node', 364)
ops.remove('node', 389)
ops.remove('node', 413)
ops.remove('node', 431)
ops.remove('node', 445)

# run analysis after object removal
ops.analyze(4)

# wipe
ops.wipe()
