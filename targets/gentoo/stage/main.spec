[collect $[path/metro]/targets/gentoo/stage/files.spec]
[collect $[path/metro]/targets/gentoo/stage/steps.spec]

[section portage]

ACCEPT_KEYWORDS: $[portage/stable]$[target/arch]

[section metro]

class: stage

[section target]

type: stage
[collect $[path/metro]/subarch/$[target/subarch].spec]

[section path]

chroot: $[path/work]
chroot/stage: $[path/work]$[portage/ROOT]