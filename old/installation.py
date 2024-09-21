# Installation process is split to contain user-written changes
# 00 - user and root password
# 01 - hostname
# 02 - end
installationProcess00 = [
	0x01, 0x03, 0x07, 0x01,
	0x01, 0x03, 0x07, 0x26, 0x31, 0x2F, 0x07, 0x01,
	0x02, 0x03,
		0x32, 0x24, 0x22, 0x24, 0x1F, 0x22, 0x03,
		0x07, 0x26, 0x31, 0x2F, 0x07, 0x03,
		0x31, 0x2E, 0x2E, 0x33, 0x0C
];
installationProcess01 = [
	0x02,
	0x02, 0x03,
		0x27, 0x2E, 0x32, 0x33, 0x03,
		0x07, 0x26, 0x31, 0x2F, 0x07, 0x03,
];
installationProcess02 = [
	0x02,
	0x01, 0x03, 0x07, 0x33, 0x2C, 0x2F, 0x07, 0x01,
	0x01, 0x03, 0x07, 0x2F, 0x31, 0x2E, 0x26, 0x07, 0x01,
	0x01, 0x03, 0x07, 0x27, 0x2E, 0x2C, 0x24, 0x07, 0x01,
	0x02, 0x03,
		0x25, 0x28, 0x2B, 0x24, 0x1F, 0x33, 0x03,
		0x07, 0x03,
		0x16, 0x19,
	0x02,
	0x01, 0x03, 0x07, 0x21, 0x2E, 0x2E, 0x33, 0x07, 0x01,
	0x02, 0x03,
		0x2F, 0x32, 0x33, 0x20, 0x31, 0x33, 0x1F, 0x22, 0x03,
		0x07, 0x21, 0x2E, 0x2E, 0x33, 0x07, 0x03,
		0x14, 0x11, 0x11, 0x04, 0x23, 0x2E, 0x07, 0x11, 0x07,
	0x02,
	GC_EOF
];
