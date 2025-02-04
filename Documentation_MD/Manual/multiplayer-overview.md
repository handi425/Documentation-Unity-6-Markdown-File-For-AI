[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/multiplayer-overview.html)
  * [中文](/cn/current/Manual/multiplayer-overview.html)
  * [日本語](/ja/current/Manual/multiplayer-overview.html)
  * [한국어](/kr/current/Manual/multiplayer-overview.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/multiplayer-overview.html)
  * [中文](/cn/current/Manual/multiplayer-overview.html)
  * [日本語](/ja/current/Manual/multiplayer-overview.html)
  * [한국어](/kr/current/Manual/multiplayer-overview.html)

  * [Multiplayer](multiplayer.html)
  * Unity multiplayer overview

[](multiplayer.html)

Multiplayer

[](multiplayer-center.html)

Use the Multiplayer Center

# Unity multiplayer overview

Unity has a number of multiplayer packages and services available to help you
create a multiplayer project. If you’re just getting started with multiplayer
games, the recommended entry point is the Multiplayer Center package.

## Getting started

### Multiplayer Center

The [Multiplayer Center](multiplayer-center.html) provides a starting point to
create a multiplayer game. It recommends Unity multiplayer packages and
services based on the needs of your game, and gives you access to samples and
tutorials to help you use them.

The Multiplayer Center package is installed in the Editor by default. It opens
automatically when you create a new multiplayer project in the Editor, or you
can open it directly using **Window** > **Multiplayer** > **Multiplayer
Center**.

### Multiplayer Services and Widgets

The [Multiplayer Services package](https://docs.unity.com/ugs/en-
us/manual/mps-sdk/manual) provides an SDK to add multiplayer elements to a
game that leverage [Unity Gaming Services
(UGS)](https://docs.unity.com/ugs/en-us/manual/overview/manual/unity-gaming-
services-home) to define how groups of players interact in your games through
Sessions. You can use the [Multiplayer Widgets
package](https://docs.unity3d.com/Packages/com.unity.multiplayer.widgets@latest?subfolder=/manual/index.html)
to easily test aspects of the workflow before further developing them
yourself.

The Multiplayer Services package is compatible by default with both Netcode
for GameObjects and Netcode for Entities, while also supporting [custom
networking solutions](https://docs.unity.com/ugs/en-us/manual/mps-
sdk/manual/create-session#Advanced_usage:_Specifying_a_custom_network_handler)
for more advanced use cases.

## Netcode for GameObjects

[Netcode for GameObjects](https://docs-
multiplayer.unity3d.com/netcode/current/about/) is a high-level **networking**
The Unity system that enables multiplayer gaming across a computer network.
[More info](multiplayer.html)  
See in [Glossary](Glossary.html#Networking) library that abstracts networking
logic and allows you to send **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) and world data across a networking
session to many players at once. It’s suitable for most types of multiplayer
project, but if you want to create a large or highly-optimized game then
Netcode for Entities might be a better choice. Netcode for GameObjects
supports both client-server and distributed authority network topologies.

Netcode for GameObjects is compatible with Multiplayer Tools, Multiplayer Play
Mode, the Dedicated Server package, and Unity’s Gaming Services.

## Netcode for Entities

[Netcode for
Entities](https://docs.unity3d.com/Packages/com.unity.netcode@latest?subfolder=/manual/index.html)
is part of Unity’s Data-Oriented Technology Stack (DOTS) and provides a
server-authoritative networking solution with a client prediction framework
that you can use to create multiplayer games. It can be used for any
multiplayer project, but is primarily recommended for large-scale games that
require heavy optimization and for advanced developers that have experience
making multiplayer games. Netcode for Entities only supports client-server
network topologies.

Netcode for Entities is compatible with Multiplayer Tools, Multiplayer Play
Mode, the Dedicated Server package, and Unity’s Gaming Services.

## Testing multiplayer games

### Multiplayer Tools

The [Multiplayer Tools package](https://docs-
multiplayer.unity3d.com/tools/current/about/) provides a variety of tools to
analyze, debug, and test your multiplayer game, including a profiler and
network simulator. You can [install the package](https://docs-
multiplayer.unity3d.com/tools/current/install-tools/) using the Unity Package
Manager, and access it from the Editor using **Window** > **Multiplayer
Tools**.

Multiplayer Tools is compatible with both Netcode for GameObjects and Netcode
for Entities.

### Multiplayer Play Mode

Use [Multiplayer Play Mode](https://docs-
multiplayer.unity3d.com/mppm/current/about/) to test multiplayer functionality
from within the Unity Editor. You can simulate up to four Players (the main
Editor Player and three Virtual Players) simultaneously on the same
development device while using the same source assets on disk. You can
[install the package](https://docs-
multiplayer.unity3d.com/mppm/current/install/) using the Unity Package
Manager, and access it from the Editor using **Window** > **Multiplayer Play
Mode**.

Multiplayer Play Mode is compatible with Netcode for GameObjects, Netcode for
Entities, the Dedicated Server package, and Unity’s Gaming Services.

## Utilities

### Unity Transport

The [Unity Transport package](https://docs-
multiplayer.unity3d.com/transport/current/about/) is a low-level networking
library for multiplayer game development. It’s the underlying protocol for
both Netcode for GameObjects and Netcode for Entities, but you can also use it
with a custom solution. Unity Transport supports all platforms the Unity
Engine supports using a connection-based abstraction layer (built-in network
driver) provided over User Datagram Protocol (UDP) and WebSockets.

You can [install the package](https://docs-
multiplayer.unity3d.com/transport/current/install/) using the Unity Package
Manager.

### Dedicated Server

The [Dedicated Server
package](https://docs.unity3d.com/Packages/com.unity.dedicated-
server@1.0/manual/index.html) allows you to switch a project between the
server and client role without the need to create another project, improving
the multiplayer development workflow when targeting the [Dedicated Server
build target](dedicated-server-introduction.html). You can install the package
using the Unity Package Manager.

The Dedicated Server package is compatible with Netcode for GameObjects,
Netcode for Entities, and Multiplayer Play Mode.

## Unity Gaming Services

The Multiplayer Services package provides an SDK to add multiplayer elements
to a game that leverage these Unity Gaming Services (UGS) to define how groups
of players interact in your games through Sessions.

### Multiplay Hosting

[Multiplay Hosting](https://docs.unity.com/ugs/en-us/manual/game-server-
hosting/manual/welcome) is Unity’s scalable server hosting platform. It’s a
self-serve experience for hosting and scaling your game that removes the
complexity of running and operating infrastructure at scale, so you can focus
on developing your multiplayer projects.

### Lobby

Unity’s [Lobby service](https://docs.unity.com/ugs/en-
us/manual/lobby/manual/unity-lobby-service) provides a way for players to
discover and connect to each other in a multiplayer game.

### Matchmaker

Unity [Matchmaker](https://docs.unity.com/ugs/en-
us/manual/matchmaker/manual/matchmaker-overview) automatically assigns remote
players to a game instance and helps you to customize your matchmaking logic.

### Relay

Unity [Relay](https://docs.unity.com/ugs/en-
us/manual/relay/manual/introduction) allows players to use a join code to
connect to a game instance. Instead of using Dedicated Game Servers, the Relay
service provides connectivity through a universal Relay server acting as a
proxy.

[](multiplayer.html)

Multiplayer

[](multiplayer-center.html)

Use the Multiplayer Center

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

