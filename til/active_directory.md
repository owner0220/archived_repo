# Active_directory란?
- Active Directory는 회사 직원들의 계정 정보와 컴퓨터에 대한 정보, 그리고 회사에서 강제하고자 하는 정책들에 대한 정보를 저장하고 있는 일종의 데이터베이스라고 생각하면 됩니다.
- 데이터베이스라고 하면 대부분 RDB를 생각하는데 Active Directory는 일반적인 데이터베이스와는 조금 다른 파일 타입의 데이터베이스이고, 암호화 되어 저장되어 있기 때문에 메모장이나 텍스트 에디터로는 열어볼 수 없습니다.
(참고로 Active Directory의 데이터베이스 파일이 저자오디는 기본위치는 도메인 컨트롤러의 C:\Windows\NTDS 폴더입니다.)

## Active Directory의 정보 확인 및 수정
- 별도의 Active Directory 관리 콘솔(MMC)들을 사용합니다
- Windows Server 2012 R2를 기준으로, 도구 옵션을 보면 Active Directory 관리 센터, Active Directory 도메인 및 트러스트, Active Directory 사용자 및 컴퓨터, Active Directory 사이트 및 서비스, ADSI 편집, DNS, 그룹 정책 관리 등의 관리 콘솔을 사용할 수 있습니다.
- 주로 Active Directory 사용자 및 컴퓨터와 그룹 정책 관리 콘솔을 사용하는데 사용자 및 컴퓨터에서는 사용자의 계정을 생성하거나, 패스워트 리셋, 컴퓨터 사용 안 함 상태를 만들어 로그온을 차단하거나 하는 등의 사용자와 컴퓨터에 대한 작업을 할 수 있습니다.
- 그룹 정책 관리 콘솔에서는 회사에서 강제하고자 하는 IT 정책들을 생성하고 적용할 수 있습니다.

## Active Directory의 용도와 활용
- 회사 전체 IT 시스템에서 사용자에 대한 인증과 권한이 필요한 부분에서는 모두 Avtive Directory의 정보를 활용합니다.

## 도입시 고려 사항
- 컴퓨터의 Active Directory 도메인 가입(Join)입니다.
- 인증과 권한 관리를 하고자 한다면 먼저 Active Directory 도메인 가입을 해야 하는데 가입을 하게 되면 사용자의 프로필이 바뀝니다. 쉽게 말하면 사용자가 기존에 로그온해서 사용하던 바탕화면과 내 문서들이 새로 생성되는데(기존의 것들은 C:\Users 하위 폴더에 남아 있습니다.) 바탕화면이 바뀌므로 공지를 하거나 별도의 도메인 가입 툴을 사용해 기존 사용자 프로필을 새 프로필로 마이그레이션 시켜야 합니다.
- 회사에서 별도로 DNS를 운영하고 있다면, Active Directory의 DNS로 마이그레이션 시켜야 합니다. Active Directory 자체가 DNS 기능을 포함하고 있으며, Active Directory에 가입된 모든 클라이언트 컴퓨터들은 Active Directory DNS를 바라보아야 합니다.  추가 사항은 개별 검색해야 합니다.

> 출처 https://mpain.tistory.com/153



## C:\Windows\NTDS 파일 설명


> 출처 http://www.rebeladmin.com/2015/02/active-directory-database-sysvol-and-system-state/
