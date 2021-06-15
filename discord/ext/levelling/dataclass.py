from typing import List, Dict

import attr


@attr.s(slots=True)
class Member(object):
    identifier: int = attr.ib(hash=True, eq=True)  # Think member.id
    xp: int = attr.ib(eq=False, default=0)
    guild_id: int = attr.ib(
        default=None,
        validator=attr.validators.optional(attr.validators.instance_of(int)),
        kw_only=True,
        eq=False,
    )

    @xp.validator
    def _validate_positive(self, attr, value):
        if value < 0:
            raise ValueError("XP must be positive")


@attr.s
class Guild:
    identifier: int = attr.ib(hash=True)  # Think guild.id
    _members: List[Member] = attr.ib(default=attr.Factory(list))
    _raw_members: List[Dict] = attr.ib(default=attr.Factory(list))

    @property
    def members(self) -> List[Member]:
        if not bool(self._members):
            for i, item in enumerate(self._raw_members):
                data = self._raw_members[i]
                # TODO Fix this shit
                self._members.append(Member(**dict(data.values())))
                print(self._members)

        return self._members
