[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Glossary.html)
  * [中文](/cn/current/Manual/Glossary.html)
  * [日本語](/ja/current/Manual/Glossary.html)
  * [한국어](/kr/current/Manual/Glossary.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Glossary.html)
  * [中文](/cn/current/Manual/Glossary.html)
  * [日本語](/ja/current/Manual/Glossary.html)
  * [한국어](/kr/current/Manual/Glossary.html)

  * Glossary

[](udp-troubleshooting.html)

UDP troubleshooting

[](Glossary.html)

Glossary

# Glossary

  * 2D terms
  * 2D Physics terms
  * AI terms
  * Analytics terms
  * Animation terms
  * Assets terms
  * Audio terms
  * Core terms
  * Editor terms
  * General terms
  * Graphics terms
  * Lighting terms
  * Multiplayer terms
  * Package Manager terms
  * Performance terms
  * Physics terms
  * Platforms terms
  * Scripting terms
  * Services terms
  * UI terms

## 2D terms

#### 2D Object:

A 2D **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) such as a **tilemap** A GameObject
that allows you to quickly create 2D levels using tiles and a grid overlay.
[More info](tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](Glossary.html#Tilemap) or **sprite** A 2D graphic objects.
If you are used to working in 3D, Sprites are essentially just standard
textures but there are special techniques for combining and managing sprite
textures for efficiency and convenience during development. [More
info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite). [More info](Unity2D.html)

#### dimetric projection:

A form of parallel projection where the dimensions of a **3D object** A 3D
GameObject such as a cube, terrain or ragdoll. [More info](GameObjects.html)  
See in [Glossary](Glossary.html#3DObject) are projected onto a 2D plane, and
only two of the three angles between the axes are equal to each other. This
form of projection is commonly used in isometric video games to simulate
three-dimensional depth. [More info](tilemaps/work-with-tilemaps/isometric-
tilemaps/isometric-tilemap-landing.html)

#### isometric projection:

A form of parallel projection where the dimensions of a **3D object** A 3D
GameObject such as a cube, terrain or ragdoll. [More info](GameObjects.html)  
See in [Glossary](Glossary.html#3DObject) are projected onto a 2D plane, and
the angles between all three axes are equal to each other. This form of
projection is commonly used in isometric video games to simulate three-
dimensional depth. [More info](tilemaps/work-with-tilemaps/isometric-
tilemaps/isometric-tilemap-landing.html)

#### sprite Atlas:

A texture that is composed of several smaller textures. Also referred to as a
texture atlas, image **sprite** A 2D graphic objects. If you are used to
working in 3D, Sprites are essentially just standard textures but there are
special techniques for combining and managing sprite textures for efficiency
and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite), **sprite** sheet or packed texture.
[More info](sprite/atlas/atlas-landing.html)

## 2D physics terms

#### Body Type:

Defines a fixed behavior for a 2D **Rigidbody** A component that allows a
GameObject to be affected by simulated gravity and other forces. [More
info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody). Can be Dynamic (the body moves
under simulation and is affected by forces like gravity), Kinematic (the body
moves under simulation, but and isn’t affected by forces like gravity) or
Static (the body doesn’t move under simulation). [More
info](2d-physics/rigidbody/introduction-to-rigidbody-2d.html)

#### Fixed Joint 2D:

A 2D **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) type which is completely constrained,
allowing two objects to be held together. Implemented as a spring so some
small motion may still occur. [More info](2d-physics/joints/fixed-
joint-2d-reference.html)

#### Physics Material 2D:

Use to adjust the friction and bounce that occurs between 2D physics objects
when they collide [More info](2d-physics/physics-material-2d-reference.html)

#### Relative Joint 2D:

A 2D **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) that allows two game objects controlled
by **Rigidbody** A component that allows a GameObject to be affected by
simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) physics to maintain in a position
based on each other’s location. Use this **joint** to keep two objects offset
from each other, at a position and angle you decide [More
info](2d-physics/joints/relative-joint-2d-reference.html)

## AI terms

#### NavMesh:

A **mesh** The main graphics primitive of Unity. Meshes make up a large part
of your 3D worlds. Unity supports triangulated or Quadrangulated polygon
meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) that Unity generates to approximate the
walkable areas and obstacles in your environment for path finding and AI-
controlled navigation. [More
info](https://docs.unity3d.com/Packages/com.unity.ai.navigation@latest/index.html?subfolder=/manual/NavInnerWorkings.html%23walkable-
areas)

## Analytics terms

#### Active Users:

Players who recently played your game. Unity **Analytics** Abbreviation of
**Unity Analytics**  
See in [Glossary](Glossary.html#Analytics) defines an active player as someone
who has played within the last 90 calendar days. [More
info](UnityAnalyticsTerminology)

#### Ad ARP:

(Average Revenue Per User) Average Unity Ads revenue per player. [More
info](UnityAnalyticsTerminology)

#### Ad Revenue:

Total Unity Ads revenue. [More info](UnityAnalyticsTerminology)

#### Ad Starts:

The number of video ads that started playing. [More
info](UnityAnalyticsTerminology)

#### Ads per DAU:

The number of ads started per active player on a given day. [More
info](UnityAnalyticsTerminology)

#### Age 14 and Under:

By default, Unity does not breakout **analytics** Abbreviation of **Unity
Analytics**  
See in [Glossary](Glossary.html#Analytics) data for players under the age of
14. See **COPPA**(Children’s Online Privacy Protection Act) COPPA is a US law
that applies to apps that collect personal information and are targeted to
children under the age of 14. [More info](UnityAnalyticsCOPPA)  
See in [Glossary](Glossary.html#COPPA) Compliance. [More
info](UnityAnalyticsTerminology)

#### All Spenders:

Players who have made any verified or unverified in-app purchases in their
lifetime. [More info](UnityAnalyticsTerminology)

#### Analytics:

Abbreviation of **Unity Analytics** A data platform that provides analytics
for your Unity game. [More info](https://docs.unity.com/ugs/en-
us/manual/analytics/manual/overview)  
See in [Glossary](Glossary.html#UnityAnalytics)

#### Analytics Events:

Events dispatched to the **Analytics** Abbreviation of **Unity Analytics**  
See in [Glossary](Glossary.html#Analytics) Service by instances of your
applications. **Analytics** events contain the data that is processed and
aggregated to provide insights into player behavior. [More
info](UnityAnalyticsCustomEvents)

#### Application version:

Player segments based on application version or bundleid. [More
info](UnityAnalyticsTerminology)

#### ARPDAU:

(Average Revenue Per Daily Active User) The average revenue per user who
played on a given day. [More info](UnityAnalyticsTerminology)

#### ARPPU:

(Average Revenue Per Paying User) Average **verified IAP revenue** Revenue
from verified IAP transactions. IAP verification is currently supported by the
Apple App Store and the Google Play Store. [More
info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#VerifiedIAPRevenue) per user who completed a
verified IAP transaction. [More info](UnityAnalyticsTerminology)

#### Churn:

The rate at which users are leaving your game during a specified period. Your
user churn is important in estimating the lifetime value of your users.
Mathematically, churn is the complement of retention (in other words: Churn +
Retention = 100%). [More info](UnityAnalyticsTerminology)

#### Cohort:

A group of players with at least one similar characteristic. You can define
and analyze different cohorts of your user base with segments. [More
info](UnityAnalyticsTerminology)

#### Conversion Rate:

The percentage of users who complete an action or sequence of actions. [More
info](UnityAnalyticsTerminology)

#### COPPA:

(Children’s Online Privacy Protection Act) **COPPA**(Children’s Online Privacy
Protection Act) COPPA is a US law that applies to apps that collect personal
information and are targeted to children under the age of 14. [More
info](UnityAnalyticsCOPPA)  
See in [Glossary](Glossary.html#COPPA) is a US law that applies to apps that
collect personal information and are targeted to children under the age of 14.
[More info](UnityAnalyticsCOPPA)

#### Core Events:

Core events are the basic events dispatched by the Unity **Analytics**
Abbreviation of **Unity Analytics**  
See in [Glossary](Glossary.html#Analytics) code in your game. These events,
and the **analytics** Abbreviation of **Unity Analytics**  
See in [Glossary](Glossary.html#Analytics) based on them, become available by
turning on Unity **Analytics** for a project. Core events include: app
running, app start, and device info. [More
info](https://docs.unity.com/ugs/en-us/manual/analytics/manual/events)

#### CTR:

(Click Through Rate) The percentage of players who click a link in an ad
displayed in your game. [More info](UnityAnalyticsTerminology)

#### Custom Events:

Custom events are freeform events that you can dispatch when an appropriate
**standard event** Standard events are application-specific events that you
dispatch in response to important player actions or milestones. Standard
events have standardized names and defined parameter lists. [More
info](UnityAnalyticsCustomEvents)  
See in [Glossary](Glossary.html#Standardevent) is not available. Custom events
can have any name and up to ten parameters. Use **standard events** Standard
events are application-specific events that you dispatch in response to
important player actions or milestones. Standard events have standardized
names and defined parameter lists. [More info](UnityAnalyticsCustomEvents)  
See in [Glossary](Glossary.html#Standardevent) in preference to custom events
where possible. [More info](UnityAnalyticsCustomEvents)

#### Data Explorer:

A Unity **Analytics** Abbreviation of **Unity Analytics**  
See in [Glossary](Glossary.html#Analytics) Dashboard page that allows you to
build, view and export reports on your **Analytics** metrics and events. You
can also see how metrics and custom events change over time. [More
info](UnityAnalyticsDataExplorer)

#### DAU:

(Daily Active Users) The number of different players who started a session on
a given day. **DAU**(Daily Active Users) The number of different players who
started a session on a given day. DAU includes both new and returning players.
[More info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#DAU) includes both new and returning players.
[More info](UnityAnalyticsTerminology)

#### DAU per MAU:

(DAU/MAU) The percentage of monthly active users who play on a given day. Also
known as **Sticky Factor** An estimate of how compelling a game is to its
players. A high “sticky factor” means that players stick with an app over
time. [More info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#StickyFactor) in the **analytics**
Abbreviation of **Unity Analytics**  
See in [Glossary](Glossary.html#Analytics) and game industries, this metric is
often used as one estimate of player engagement. [More
info](UnityAnalyticsTerminology)

#### Day 1 Retention:

The percentage of players who returned to your game one day after playing the
first time. [More info](UnityAnalyticsTerminology)

#### Day 30 Retention:

The percentage of players who returned to your game thirty days after playing
the first time. [More info](UnityAnalyticsTerminology)

#### Day 7 Retention:

The percentage of players who returned to your game seven days after playing
the first time. [More info](UnityAnalyticsTerminology)

#### Demographics:

Player segments based on reported demographics. [More
info](UnityAnalyticsTerminology)

#### Dolphins:

Players who have spent between $5 and $19.99. [More
info](UnityAnalyticsTerminology)

#### eCPM:

(estimated Cost Per Mille) The estimated revenue for 1000 ad impressions for
your app. [More info](UnityAnalyticsTerminology)

#### Engagement:

Engagement is a broad measure of how players enjoy, or are otherwise invested,
in your game. Impossible to measure directly, the following metrics are
frequently used to estimate engagement: Retention, **DAU**(Daily Active Users)
The number of different players who started a session on a given day. DAU
includes both new and returning players. [More
info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#DAU), **MAU**(Monthly Active Users) The number
of players who started a session within the last 30 days. [More
info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#MAU), **DAU** /**MAU** , number of sessions,
and session length. [More info](UnityAnalyticsTerminology)

#### F2P:

(Free to Play) A business model that offers users free access to a fully
functional game and a significant portion of app content. Monetization
strategies for these titles generally include microtransactions that allow
users to access premium features and virtual goods. [More
info](UnityAnalyticsTerminology)

#### Fill Rate:

The rate at which ads are available when you request one. [More
info](UnityAnalyticsTerminology)

#### Funnel:

In **Analytics** Abbreviation of **Unity Analytics**  
See in [Glossary](Glossary.html#Analytics), a funnel is a linear sequence of
standard or custom events that you expect a player to complete in order. [More
info](UnityAnalyticsFunnels)

#### Geography:

Player segments based on country. [More info](UnityAnalyticsTerminology)

#### Heatmaps:

Heatmaps are a spatial visualization of **analytics** Abbreviation of **Unity
Analytics**  
See in [Glossary](Glossary.html#Analytics) data. [More
info](UnityAnalyticsOverview#Heatmaps)

#### IAP:

See **In App Purchase** Revenue from “micro-transactions” within a game. [More
info](UnityIAP.html)  
See in [Glossary](Glossary.html#InAppPurchase)

#### In App Purchase:

Revenue from “micro-transactions” within a game. [More info](UnityIAP.html)

#### Impressions:

The number of times ads are seen in your game. An impression is counted even
if the ad is not completed. [More info](UnityAnalyticsTerminology)

#### LTV:

(Lifetime Value) The estimated value of an average player over their lifetime
with your application or game. [More info](UnityAnalyticsTerminology)

#### MAU:

(Monthly Active Users) The number of players who started a session within the
last 30 days. [More info](UnityAnalyticsTerminology)

#### Minnow:

A player who has spent less than $5 in their lifetime. [More
info](UnityAnalyticsTerminology)

#### Never Monetized:

Players who have never spent real currency. [More
info](UnityAnalyticsTerminology)

#### New Users:

Users who played your game for the first time. [More
info](UnityAnalyticsTerminology)

#### Number of Unverified Transactions:

The total number of IAP transactions, whether or not they have been verified.
[More info](UnityAnalyticsTerminology)

#### Number of Users:

The cumulative number of unique players over the last 90 days. Users who have
not played in more than 90 days are removed from the count. [More
info](UnityAnalyticsTerminology)

#### Number of Verified Transactions:

IAP transactions that have been verified through the appropriate app store.
IAP verification is currently supported by the Apple App Store and the Google
Play Store. [More info](UnityAnalyticsTerminology)

#### Percentage of Population:

Your player population as a percentage. Typically only useful when combined
with a segment. Calculated as the percentage of the Number of Users metric who
are members of a specified segment. [More info](UnityAnalyticsTerminology)

#### Remote Settings:

Remote settings are game variables that you can set remotely on your
**Analytics** Abbreviation of **Unity Analytics**  
See in [Glossary](Glossary.html#Analytics) Dashboard. [More
info](UnityAnalyticsRemoteSettings)

#### Segment:

Segments are subsets of your player base, split apart by key differentiators.
Viewing metrics and events by segment can reveal differences in-game behavior
between different groups. [More info](UnityAnalyticsTerminology)

#### Session:

A single play or usage period. A new session is counted when a player launches
your game or brings a suspended game to the foreground after 30 minutes of
inactivity. [More info](UnityAnalyticsTerminology)

#### Sessions per User:

The average number of sessions per person playing on a given day. Also known
as Average Number of Sessions per **DAU**(Daily Active Users) The number of
different players who started a session on a given day. DAU includes both new
and returning players. [More info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#DAU). [More info](UnityAnalyticsTerminology)

#### Standard event:

Standard events are application-specific events that you dispatch in response
to important player actions or milestones. **Standard events** Standard events
are application-specific events that you dispatch in response to important
player actions or milestones. Standard events have standardized names and
defined parameter lists. [More info](UnityAnalyticsCustomEvents)  
See in [Glossary](Glossary.html#Standardevent) have standardized names and
defined parameter lists. [More info](UnityAnalyticsCustomEvents)

#### Sticky Factor:

An estimate of how compelling a game is to its players. A high “**sticky
factor** An estimate of how compelling a game is to its players. A high
”sticky factor“ means that players stick with an app over time. [More
info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#StickyFactor)” means that players stick with
an app over time. [More info](UnityAnalyticsTerminology)

#### Total Daily Playing Time:

The cumulative playing time of all people playing on a given day. [More
info](UnityAnalyticsTerminology)

#### Total Daily Playing Time per Active User:

The average playing time of people playing on a given day. [More
info](UnityAnalyticsTerminology)

#### Total IAP Revenue:

The **total IAP revenue** The total IAP revenue, including revenue from both
verified and unverified transactions. [More info](UnityAnalyticsTerminology)  
See in [Glossary](Glossary.html#TotalIAPRevenue), including revenue from both
verified and unverified transactions. [More info](UnityAnalyticsTerminology)

#### Total Sessions Today:

The total number of sessions by all people playing on a given day. Also known
as Total Sessions. [More info](UnityAnalyticsTerminology)

#### Total Verified Revenue:

Revenue from Unity Ads and verified IAP transactions. IAP verification is
currently supported by the Apple App Store and the Google Play Store. [More
info](UnityAnalyticsTerminology)

#### Unity Analytics:

A data platform that provides **analytics** Abbreviation of **Unity
Analytics**  
See in [Glossary](Glossary.html#Analytics) for your Unity game. [More
info](https://docs.unity.com/ugs/en-us/manual/analytics/manual/overview)

#### Unity IAP:

Abbreviation of Unity **In App Purchase** Revenue from “micro-transactions”
within a game. [More info](UnityIAP.html)  
See in [Glossary](Glossary.html#InAppPurchase)

#### Unknown Gender:

Players to whom you have assigned Gender.Unknown. (Players whose gender has
not been reported at all are not included in this segment.) [More
info](UnityAnalyticsTerminology)

#### Unverified IAP Revenue:

IAP revenue from sources that do not support verification and from
transactions that failed verification. Transactions can fail verification
because they are fraudulent or because of missing or malformed information.
[More info](UnityAnalyticsTerminology)

#### Verified IAP Revenue:

Revenue from verified IAP transactions. IAP verification is currently
supported by the Apple App Store and the Google Play Store. [More
info](UnityAnalyticsTerminology)

#### Verified Paying Users:

Players who made verified IAP purchases. IAP verification is currently
supported by the Apple App Store and the Google Play Store. [More
info](UnityAnalyticsTerminology)

#### Whales:

Players who have spent at least $20 in their lifetime. [More
info](UnityAnalyticsTerminology)

## Animation terms

#### 1D Blend Tree:

A Blend Tree for 1D blending, which blends motion according to a single
Animation Parameter. [More info](BlendTree-1DBlending.html)

#### 2D Blend Tree:

A Blend Tree for 2D blending, which blends motion according to two **Animation
Parameters** Used to communicate between scripting and the Animator
Controller. Some parameters can be set in scripting and used by the
controller, while other parameters are based on Custom Curves in Animation
Clips and can be sampled using the scripting API. [More
info](AnimationParameters.html)  
See in [Glossary](Glossary.html#AnimationParameters). [More
info](BlendTree-2DBlending.html)

#### 3D Object:

A 3D **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) such as a cube, **terrain** The
landscape in your scene. A Terrain GameObject adds a large flat plane to your
scene and you can use the Terrain’s Inspector window to create a detailed
landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) or ragdoll. [More
info](GameObjects.html)

#### Animation Blend Shape:

Enables you to make an object change its form by blending between two separate
meshes. [More info](BlendShapes.html)

#### Animation Blend Tree:

Used for continuous blending between similar **Animation Clips** Animation
data that can be used for animated characters or simple animations. It is a
simple “unit” piece of motion, such as (one specific instance of) “Idle”,
“Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) based on float **Animation
Parameters** Used to communicate between scripting and the Animator
Controller. Some parameters can be set in scripting and used by the
controller, while other parameters are based on Custom Curves in Animation
Clips and can be sampled using the scripting API. [More
info](AnimationParameters.html)  
See in [Glossary](Glossary.html#AnimationParameters). [More info](class-
BlendTree.html)

#### Animation Clip:

Animation data that can be used for animated characters or simple animations.
It is a simple “unit” piece of motion, such as (one specific instance of)
“Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)

#### Animation Clip Node:

A node in a Blend Tree graph that contains an **animation clip** Animation
data that can be used for animated characters or simple animations. It is a
simple “unit” piece of motion, such as (one specific instance of) “Idle”,
“Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip), such as a run or walk
animation. [More info](class-BlendTree.html)

#### animation compression:

The method of compressing animation data to significantly reduce file sizes
without causing a noticeable reduction in motion quality. Animation
**compression** A method of storing data that reduces the amount of storage
space it requires. See [Texture Compression](class-TextureImporterOverride),
[Animation Compression](class-AnimationClip.html#AssetProperties), [Audio
Compression](class-AudioClip.html), [Build
Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) is a trade off between saving on
memory and image quality. [More info](class-
AnimationClip.html#AssetProperties)

#### Animation Curves:

Allows you to add data to an imported clip so you can animate the timings of
other items based on the state of an animator. For example, for a game set in
icy conditions, you could use an extra animation curve to control the emission
rate of a **particle system** A component that simulates fluid entities such
as liquids, clouds and flames by generating and animating large numbers of
small 2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) to show the player’s
condensing breath in the cold air. [More
info](AnimationCurvesOnImportedClips.html)

#### Animation Event:

Allows you to add data to an imported clip which determines when certain
actions should occur in time with the animation. For example, for an animated
character you might want to add events to walk and run cycles to indicate when
the footstep sounds should play. [More
info](AnimationEventsOnImportedClips.html)

#### Animation Layer:

An **Animation Layer** An Animation Layer contains an Animation State Machine
that controls animations of a model or part of it. An example of this is if
you have a full-body layer for walking or jumping and a higher layer for
upper-body motions such as throwing an object or shooting. The higher layers
take precedence for the body parts they control. [More
info](AnimationLayers.html)  
See in [Glossary](Glossary.html#AnimationLayer) contains an Animation **State
Machine** The set of states in an Animator Controller that a character or
animated GameObject can be in, along with a set of transitions between those
states and a variable to remember the current state. The states available will
depend on the type of gameplay, but typical states include things like idling,
walking, running and jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) that controls animations of a
model or part of it. An example of this is if you have a full-body layer for
walking or jumping and a higher layer for upper-body motions such as throwing
an object or shooting. The higher layers take precedence for the body parts
they control. [More info](AnimationLayers.html)

#### Animation Parameters:

Used to communicate between scripting and the **Animator Controller** Controls
animation through Animation Layers with Animation State Machines and Animation
Blend Trees, controlled by Animation Parameters. The same Animator Controller
can be referenced by multiple models with Animator components. [More
info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController). Some parameters can be
set in scripting and used by the controller, while other parameters are based
on Custom Curves in **Animation Clips** Animation data that can be used for
animated characters or simple animations. It is a simple “unit” piece of
motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More
info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) and can be sampled using the
scripting API. [More info](AnimationParameters.html)

#### Animation State Machine:

A graph within an **Animator Controller** Controls animation through Animation
Layers with Animation State Machines and Animation Blend Trees, controlled by
Animation Parameters. The same Animator Controller can be referenced by
multiple models with Animator components. [More info](class-
AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController) that controls the
interaction of Animation States. Each state references an **Animation Blend
Tree** Used for continuous blending between similar Animation Clips based on
float Animation Parameters. [More info](class-BlendTree.html)  
See in [Glossary](Glossary.html#AnimationBlendTree) or a single **Animation
Clip** Animation data that can be used for animated characters or simple
animations. It is a simple “unit” piece of motion, such as (one specific
instance of) “Idle”, “Walk” or “Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip). [More
info](AnimationStateMachines.html)

#### Animation Transition:

Allows a **state machine** The set of states in an Animator Controller that a
character or animated GameObject can be in, along with a set of transitions
between those states and a variable to remember the current state. The states
available will depend on the type of gameplay, but typical states include
things like idling, walking, running and jumping. [More
info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) to switch or blend from one
animation state to another. Transitions define how long a blend between states
should take, and the conditions that activate them. [More
info](StateMachineTransitions.html)

#### Animator Component:

A component on a model that animates that model using the Animation system.
The component has a reference to an **Animator Controller** Controls animation
through Animation Layers with Animation State Machines and Animation Blend
Trees, controlled by Animation Parameters. The same Animator Controller can be
referenced by multiple models with Animator components. [More info](class-
AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController) asset that controls the
animation. [More info](class-AnimatorController.html)

#### Animator Controller:

Controls animation through **Animation Layers** An Animation Layer contains an
Animation State Machine that controls animations of a model or part of it. An
example of this is if you have a full-body layer for walking or jumping and a
higher layer for upper-body motions such as throwing an object or shooting.
The higher layers take precedence for the body parts they control. [More
info](AnimationLayers.html)  
See in [Glossary](Glossary.html#AnimationLayer) with Animation **State
Machines** The set of states in an Animator Controller that a character or
animated GameObject can be in, along with a set of transitions between those
states and a variable to remember the current state. The states available will
depend on the type of gameplay, but typical states include things like idling,
walking, running and jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) and **Animation Blend Trees**
Used for continuous blending between similar Animation Clips based on float
Animation Parameters. [More info](class-BlendTree.html)  
See in [Glossary](Glossary.html#AnimationBlendTree), controlled by **Animation
Parameters** Used to communicate between scripting and the Animator
Controller. Some parameters can be set in scripting and used by the
controller, while other parameters are based on Custom Curves in Animation
Clips and can be sampled using the scripting API. [More
info](AnimationParameters.html)  
See in [Glossary](Glossary.html#AnimationParameters). The same **Animator
Controller** Controls animation through Animation Layers with Animation State
Machines and Animation Blend Trees, controlled by Animation Parameters. The
same Animator Controller can be referenced by multiple models with Animator
components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController) can be referenced by
multiple models with **Animator components** A component on a model that
animates that model using the Animation system. The component has a reference
to an Animator Controller asset that controls the animation. [More
info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorComponent). [More info](class-
AnimatorController.html)

#### Animator Override Controller:

Allows you to create multiple variants of an **Animator Controller** Controls
animation through Animation Layers with Animation State Machines and Animation
Blend Trees, controlled by Animation Parameters. The same Animator Controller
can be referenced by multiple models with Animator components. [More
info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController), with each variant using a
different set of animations, while retaining the original Controller’s
structure, parameters and logic. [More info](AnimatorOverrideController.html)

#### Animator Window:

The window where the **Animator Controller** Controls animation through
Animation Layers with Animation State Machines and Animation Blend Trees,
controlled by Animation Parameters. The same Animator Controller can be
referenced by multiple models with Animator components. [More info](class-
AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController) is visualized and edited.
[More info](AnimatorWindow.html)

#### Avatar:

An interface for **retargeting** Applying animations created for one model to
another. [More info](Retargeting.html)  
See in [Glossary](Glossary.html#Retargeting) animation from one rig to
another. [More info](ConfiguringtheAvatar.html)

#### Avatar Mask:

A specification for which body parts to include or exclude for an animation
rig. Used in **Animation Layers** An Animation Layer contains an Animation
State Machine that controls animations of a model or part of it. An example of
this is if you have a full-body layer for walking or jumping and a higher
layer for upper-body motions such as throwing an object or shooting. The
higher layers take precedence for the body parts they control. [More
info](AnimationLayers.html)  
See in [Glossary](Glossary.html#AnimationLayer) and in the importer. [More
info](class-AvatarMask.html)

#### Bind-pose:

The pose at which the character was modelled.

#### blend:

Transition from one animation to another animation smoothly and seamlessly,
such as blending a character’s walking and running animations according to the
character’s speed.

#### Blend Node:

A node in a Blend Tree graph that blends **animation clip** Animation data
that can be used for animated characters or simple animations. It is a simple
“unit” piece of motion, such as (one specific instance of) “Idle”, “Walk” or
“Run”. [More info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) nodes. [More info](class-
BlendTree.html)

#### Body Transform:

The mass center of the character. It is used in for animation **retargeting**
Applying animations created for one model to another. [More
info](Retargeting.html)  
See in [Glossary](Glossary.html#Retargeting) and provides the most stable
displacement model. [More info](RootMotion.html)

#### Direct Blend Tree:

A Blend Tree that allows you to map animator parameters directly to the weight
of a Blend Tree child. This is useful when you want to have exact control over
the animations that are being blended rather than blend them indirectly using
one or two parameters (in the case of 1D and 2D blend trees). [More
info](BlendTree-DirectBlending.html)

#### forward kinematics:

A method of posing a skeleton for animation by rotating the **joint** A
physics component allowing a dynamic connection between Rigidbody components,
usually allowing some degree of movement such as a hinge. [More
info](Joints.html)  
See in [Glossary](Glossary.html#joint) angles to predetermined values. The
position of a child **joint** changes according to the rotation of its parent
and so the end point of a chain of **joints** A physics component allowing a
dynamic connection between Rigidbody components, usually allowing some degree
of movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) can be determined from the angles and
relative positions of the individual **joints** it contains.

#### Human template:

A pre-defined bone-mapping. Used for matching bones from FBX files to the
**Avatar** An interface for retargeting animation from one rig to another.
[More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar). [More info](class-HumanTemplate.html)

#### Humanoid animation:

An animation using humanoid skeletons. Humanoid models generally have the same
basic structure, representing the major articulate parts of the body, head and
limbs. This makes it easy to map animations from one humanoid skeleton to
another, allowing **retargeting** Applying animations created for one model to
another. [More info](Retargeting.html)  
See in [Glossary](Glossary.html#Retargeting) and inverse **kinematics** The
geometry that describes the position and orientation of a character’s joints
and bodies. Used by inverse kinematics to control character movement.  
See in [Glossary](Glossary.html#kinematics). [More
info](ConfiguringtheAvatar.html)

#### inverse kinematics (IK):

The automatic calculation of **joint** A physics component allowing a dynamic
connection between Rigidbody components, usually allowing some degree of
movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) angles (eg. the shoulder and elbow
joint of an arm) so that the end point (eg. the hand) reaches a desired point
in space. In contrast to **Forward Kinematics** A method of posing a skeleton
for animation by rotating the joint angles to predetermined values. The
position of a child joint changes according to the rotation of its parent and
so the end point of a chain of joints can be determined from the angles and
relative positions of the individual joints it contains.  
See in [Glossary](Glossary.html#forwardkinematics) [More
info](InverseKinematics.html)

#### keyframe:

A frame that marks the start or end point of a transition in an animation.
Frames in between the **keyframes** A frame that marks the start or end point
of a transition in an animation. Frames in between the keyframes are called
inbetweens.  
See in [Glossary](Glossary.html#keyframe) are called inbetweens.

#### Keyframe Reduction:

A process that removes redundant **keyframes** A frame that marks the start or
end point of a transition in an animation. Frames in between the keyframes are
called inbetweens.  
See in [Glossary](Glossary.html#keyframe). [More info](class-
AnimationClip.html#AssetProperties)

#### kinematics:

The geometry that describes the position and orientation of a character’s
**joints** A physics component allowing a dynamic connection between Rigidbody
components, usually allowing some degree of movement such as a hinge. [More
info](Joints.html)  
See in [Glossary](Glossary.html#joint) and bodies. Used by inverse
**kinematics** The geometry that describes the position and orientation of a
character’s joints and bodies. Used by inverse kinematics to control character
movement.  
See in [Glossary](Glossary.html#kinematics) to control character movement.

#### Loop Pose:

An **animation clip** Animation data that can be used for animated characters
or simple animations. It is a simple “unit” piece of motion, such as (one
specific instance of) “Idle”, “Walk” or “Run”. [More info](class-
AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) setting that blends the end and
start of an animation to create a seamless join. [More info](class-
AnimationClip.html)

#### Muscle definition:

This allows you to have more intuitive control over the character’s skeleton.
When an **Avatar** An interface for retargeting animation from one rig to
another. [More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar) is in place, the Animation system
works in muscle space, which is more intuitive than bone space. [More
info](MuscleDefinitions.html)

#### Ping Pong:

To repeatedly play an animation to the end, then in reverse back to the
beginning, in a loop.

#### Playable Graph:

An API for controlling **Playables** An API that provides a way to create
tools, effects or other gameplay mechanisms by organizing and evaluating data
sources in a tree-like structure known as the PlayableGraph. [More
info](Playables.html)  
See in [Glossary](Glossary.html#Playables). **Playable Graphs** An API for
controlling Playables. Playable Graphs allow you to create, connect and
destroy playables. [More info](Playables-Graph.html)  
See in [Glossary](Glossary.html#PlayableGraph) allow you to create, connect
and destroy **playables** An API that provides a way to create tools, effects
or other gameplay mechanisms by organizing and evaluating data sources in a
tree-like structure known as the PlayableGraph. [More info](Playables.html)  
See in [Glossary](Glossary.html#Playables). [More info](Playables-Graph.html)

#### Playables:

An API that provides a way to create tools, effects or other gameplay
mechanisms by organizing and evaluating data sources in a tree-like structure
known as the PlayableGraph. [More info](Playables.html)

#### Retargeting:

Applying animations created for one model to another. [More
info](Retargeting.html)

#### Rigging:

The process of building a skeleton hierarchy of **joints** A physics component
allowing a dynamic connection between Rigidbody components, usually allowing
some degree of movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) for your **mesh** The main graphics
primitive of Unity. Meshes make up a large part of your 3D worlds. Unity
supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv
surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh). Performed with an external tool, such
as Blender or Autodesk Maya. [More info](UsingHumanoidChars.html)

#### Root Motion:

Motion of character’s **root node** A transform in an animation hierarchy that
allows Unity to establish consistency between Animation clips for a generic
model. It also enables Unity to properly blend between Animations that have
not been authored “in place” (that is, where the whole Model moves its world
position while animating). [More
info](AnimationRootMotionNodeOnImportedClips.html)  
See in [Glossary](Glossary.html#Rootnode), whether it’s controlled by the
animation itself or externally. [More info](RootMotion.html)

#### Root node:

A transform in an animation hierarchy that allows Unity to establish
consistency between **Animation clips** Animation data that can be used for
animated characters or simple animations. It is a simple “unit” piece of
motion, such as (one specific instance of) “Idle”, “Walk” or “Run”. [More
info](class-AnimationClip.html)  
See in [Glossary](Glossary.html#AnimationClip) for a generic model. It also
enables Unity to properly blend between Animations that have not been authored
“in place” (that is, where the whole Model moves its world position while
animating). [More info](AnimationRootMotionNodeOnImportedClips.html)

#### Root Transform:

The Transform at the top of a hierarchy of Transforms. In a **Prefab** An
asset type that allows you to store a GameObject complete with components and
properties. The prefab acts as a template from which you can create new object
instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab), the **Root Transform** The Transform
at the top of a hierarchy of Transforms. In a Prefab, the Root Transform is
the topmost Transform in the Prefab. In an animated humanoid character, the
Root Transform is a projection on the Y plane of the Body Transform and is
computed at run time. At every frame, a change in the Root Transform is
computed, and then this is applied to the GameObject to make it move. [More
info](RootMotion.html)  
See in [Glossary](Glossary.html#RootTransform) is the topmost Transform in the
**Prefab**. In an animated humanoid character, the **Root Transform** is a
projection on the Y plane of the Body Transform and is computed at run time.
At every frame, a change in the **Root Transform** is computed, and then this
is applied to the **GameObject** The fundamental object in Unity scenes, which
can represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to make it move. [More
info](RootMotion.html)

#### Scene:

A **Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) contains the environments and menus of
your game. Think of each unique **Scene** file as a unique level. In each
**Scene** , you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)

#### Skinning:

The process of binding bone **joints** A physics component allowing a dynamic
connection between Rigidbody components, usually allowing some degree of
movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) to the vertices of a character’s
**mesh** The main graphics primitive of Unity. Meshes make up a large part of
your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes.
Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) or ‘skin’. Performed with an external
tool, such as Blender or Autodesk Maya. [More info](UsingHumanoidChars.html)

#### State Machine:

The set of states in an **Animator Controller** Controls animation through
Animation Layers with Animation State Machines and Animation Blend Trees,
controlled by Animation Parameters. The same Animator Controller can be
referenced by multiple models with Animator components. [More info](class-
AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController) that a character or
animated **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) can be in, along with a set of
transitions between those states and a variable to remember the current state.
The states available will depend on the type of gameplay, but typical states
include things like idling, walking, running and jumping. [More
info](StateMachineBasics.html)

#### State Machine Behaviour:

A script that attaches to a state within a **state machine** The set of states
in an Animator Controller that a character or animated GameObject can be in,
along with a set of transitions between those states and a variable to
remember the current state. The states available will depend on the type of
gameplay, but typical states include things like idling, walking, running and
jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine) to control what happens when the
**state machine** enters, exits or remains within a state, such as play sounds
as states are entered. [More info](StateMachineBehaviours.html)

#### T-pose:

The pose in which the character has their arms straight out to the sides,
forming a “T”. The required pose for the character to be in, in order to make
an **Avatar** An interface for retargeting animation from one rig to another.
[More info](ConfiguringtheAvatar.html)  
See in [Glossary](Glossary.html#Avatar).

#### Target matching:

A scripting function that allows you to move characters in such a way that a
hand or foot lands in a certain place at a certain time. For example, the
character may need to jump across stepping stones or jump and grab an overhead
beam. [More info](TargetMatching.html)

#### Transition:

The blend from one state to another in a **state machine** The set of states
in an Animator Controller that a character or animated GameObject can be in,
along with a set of transitions between those states and a variable to
remember the current state. The states available will depend on the type of
gameplay, but typical states include things like idling, walking, running and
jumping. [More info](StateMachineBasics.html)  
See in [Glossary](Glossary.html#StateMachine), such as transitioning a
character from a walk to a jog animation. Transitions define how long the
blend between states should take, and the conditions that activate the blend.
[More info](class-Transition.html)

#### Translate DoF:

The three degrees-of-freedom associated with translation (movement in X,Y & Z)
as opposed to rotation.

## Asset terms

#### Accelerator:

The Unity **Accelerator** The Unity Accelerator is an external tool that
provides an asset cache that keeps copies of a team’s imported assets. The
goal of the Accelerator is to speed up teamwork and reduce iteration time by
coordinating asset sharing so that you don’t need to reimport portions of your
project. [More info](UnityAccelerator.html)  
See in [Glossary](Glossary.html#Accelerator) is an external tool that provides
an asset cache that keeps copies of a team’s imported assets. The goal of the
**Accelerator** is to speed up teamwork and reduce iteration time by
coordinating asset sharing so that you don’t need to reimport portions of your
project. [More info](UnityAccelerator.html)

#### Asset:

Any media or data that can be used in your game or project. An asset may come
from a file created outside of Unity, such as a 3D Model, an audio file or an
image. You can also create some asset types in Unity, such as an **Animator
Controller** Controls animation through Animation Layers with Animation State
Machines and Animation Blend Trees, controlled by Animation Parameters. The
same Animator Controller can be referenced by multiple models with Animator
components. [More info](class-AnimatorController.html)  
See in [Glossary](Glossary.html#AnimatorController), an Audio Mixer or a
**Render Texture** A special type of Texture that is created and updated at
runtime. To use them, first create a new Render Texture and designate one of
your Cameras to render into it. Then you can use the Render Texture in a
Material just like a regular Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture). [More
info](AssetWorkflow.html)

#### Asset package:

A collection of files and data from Unity projects, or elements of projects,
which are compressed and stored in one file, similar to Zip files, with the
`.unitypackage` extension. **Asset packages** A collection of files and data
from Unity projects, or elements of projects, which are compressed and stored
in one file, similar to Zip files, with the `.unitypackage` extension. Asset
packages are a handy way of sharing and re-using Unity projects and
collections of assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage) are a handy way of sharing and
re-using Unity projects and collections of assets. [More
info](AssetPackages.html)

#### Asset Server:

Legacy - An asset and **version control** A system for managing file changes.
You can use Unity in conjunction with most common version control tools,
including Perforce, Git, Mercurial and PlasticSCM. [More
info](VersionControl.html)  
See in [Glossary](Glossary.html#VersionControl) system with a graphical user
interface integrated into Unity. Enables team members to work together on a
project on different computers.

#### Asset Store:

A growing library of free and commercial assets created by Unity and members
of the community. Offers a wide variety of assets, from textures, models and
animations to whole project examples, tutorials and Editor extensions. [More
info](AssetStore.html)

#### Asset Store package:

A bundled collection of assets or tools available for purchase or download on
the Unity **Asset Store** A growing library of free and commercial assets
created by Unity and members of the community. Offers a wide variety of
assets, from textures, models and animations to whole project examples,
tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore), compressed and stored as an
**asset package** A collection of files and data from Unity projects, or
elements of projects, which are compressed and stored in one file, similar to
Zip files, with the `.unitypackage` extension. Asset packages are a handy way
of sharing and re-using Unity projects and collections of assets. [More
info](AssetPackages.html)  
See in [Glossary](Glossary.html#Assetpackage) (`.unitypackage` extension) or a
**UPM package** A **Package** managed by the **Unity Package Manager**. Refer
to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage). You can manage your packages from
the **Asset Store** either on the online store or through the Package Manager
window. [More info](AssetStorePackages.html)

#### Model:

A 3D model representation of an object, such as a character, a building, or a
piece of furniture. [More info](3D-formats.html)

#### Model file:

A file containing a 3D data, which may include definitions for meshes, bones,
animation, materials and textures. [More info](3D-formats.html)

#### Package:

A container that stores various types of features and assets for Unity,
including Editor or Runtime tools and libraries, Asset collections, and
project templates. Packages are self-contained units that the Unity Package
Manager can share across Unity projects. Most of the time these are called
_packages_ , but occasionally they are called **Unity Package Manager (UPM)
packages**. [More info](Packages.html)

#### Prefab:

An asset type that allows you to store a **GameObject** The fundamental object
in Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) complete with components and
properties. The **prefab** An asset type that allows you to store a GameObject
complete with components and properties. The prefab acts as a template from
which you can create new object instances in the scene. [More
info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab) acts as a template from which you can
create new object instances in the **scene** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). [More info](Prefabs.html)

#### Unity unit:

The unit size used in Unity projects. By default, 1 **Unity unit** The unit
size used in Unity projects. By default, 1 Unity unit is 1 meter. To use a
different scale, set the Scale Factor in the Import Settings when importing
assets.  
See in [Glossary](Glossary.html#Unityunit) is 1 meter. To use a different
scale, set the Scale Factor in the Import Settings when importing assets.

#### UPM package:

A **Package** A container that stores various types of features and assets for
Unity, including Editor or Runtime tools and libraries, Asset collections, and
project templates. Packages are self-contained units that the Unity Package
Manager can share across Unity projects. Most of the time these are called
_packages_ , but occasionally they are called **Unity Package Manager (UPM)
packages**. [More info](Packages.html)  
See in [Glossary](Glossary.html#Package) managed by the **Unity Package
Manager**. Refer to **Packages** Packages are collections of assets to be
shared and re-used in Unity. The [Unity Package Manager](upm-ui.html) (UPM)
can display, add, and remove packages from your project. These packages are
native to the Unity Package Manager and provide a fundamental method of
delivering Unity functionality. However, the Unity Package Manager can also
display [Asset Store packages](AssetStorePackages.html) that you downloaded
from the Asset Store. [More info](Packages.html)  
See in [Glossary](Glossary.html#Packages).

## Audio terms

#### Audio Clip:

A container for audio data in Unity. Unity supports mono, stereo and
multichannel audio assets (up to eight channels). Unity can import .aif, .wav,
.mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module
formats. [More info](class-AudioClip.html)

#### Audio Distortion Filter:

An **audio filter** Any audio filter that distorts the sound from an Audio
Source or sounds reaching the Audio Listener. [More info](class-
AudioEffect.html)  
See in [Glossary](Glossary.html#AudioFilter) that distorts the sound from an
**Audio Source** A component which plays back an Audio Clip in the scene to an
audio listener or through an audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource) or sounds reaching the **Audio
Listener** A component that acts like a microphone, receiving sound from Audio
Sources in the scene and outputting to the computer speakers. [More
info](class-AudioListener.html)  
See in [Glossary](Glossary.html#AudioListener) by simulating the sound of a
low quality radio transmission. [More info](class-AudioDistortionFilter.html)

#### Audio Effect:

Any effect that can modify the output of Audio Mixer components, such as
filtering frequency ranges of a sound or applying reverb. [More info](class-
AudioEffectMixer.html)

#### Audio Filter:

Any **audio filter** Any audio filter that distorts the sound from an Audio
Source or sounds reaching the Audio Listener. [More info](class-
AudioEffect.html)  
See in [Glossary](Glossary.html#AudioFilter) that distorts the sound from an
**Audio Source** A component which plays back an Audio Clip in the scene to an
audio listener or through an audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource) or sounds reaching the **Audio
Listener** A component that acts like a microphone, receiving sound from Audio
Sources in the scene and outputting to the computer speakers. [More
info](class-AudioListener.html)  
See in [Glossary](Glossary.html#AudioListener). [More info](class-
AudioEffect.html)

#### Audio High Pass Filter:

An **audio filter** Any audio filter that distorts the sound from an Audio
Source or sounds reaching the Audio Listener. [More info](class-
AudioEffect.html)  
See in [Glossary](Glossary.html#AudioFilter) that passes high frequencies of
an AudioSource and cuts off signals with frequencies lower than the Cutoff
Frequency. [More info](class-AudioHighPassFilter.html)

#### Audio Listener:

A component that acts like a microphone, receiving sound from **Audio
Sources** A component which plays back an Audio Clip in the scene to an audio
listener or through an audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource) in the **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) and outputting to the computer
speakers. [More info](class-AudioListener.html)

#### Audio Low Pass Filter:

An **audio filter** Any audio filter that distorts the sound from an Audio
Source or sounds reaching the Audio Listener. [More info](class-
AudioEffect.html)  
See in [Glossary](Glossary.html#AudioFilter) that passes low frequencies of an
**Audio Source** A component which plays back an Audio Clip in the scene to an
audio listener or through an audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource) or all sound reaching an **Audio
Listener** A component that acts like a microphone, receiving sound from Audio
Sources in the scene and outputting to the computer speakers. [More
info](class-AudioListener.html)  
See in [Glossary](Glossary.html#AudioListener) while removing frequencies
higher than the Cutoff Frequency. [More info](class-AudioLowPassFilter.html)

#### Audio Source:

A component which plays back an **Audio Clip** A container for audio data in
Unity. Unity supports mono, stereo and multichannel audio assets (up to eight
channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and
.xm, .mod, .it, and .s3m tracker module formats. [More info](class-
AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip) in the **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) to an **audio listener** A component
that acts like a microphone, receiving sound from Audio Sources in the scene
and outputting to the computer speakers. [More info](class-AudioListener.html)  
See in [Glossary](Glossary.html#AudioListener) or through an audio mixer.
[More info](class-AudioSource.html)

#### Audio Spatializer:

A **plug-in** A set of code created outside of Unity that creates
functionality in Unity. There are two kinds of plug-ins you can use in Unity:
Managed plug-ins (managed .NET assemblies created with tools like Visual
Studio) and Native plug-ins (platform-specific native code libraries). [More
info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) that changes the way audio is
transmitted from an **audio source** A component which plays back an Audio
Clip in the scene to an audio listener or through an audio mixer. [More
info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource) into the surrounding space. It
takes the source and regulates the gains of the left and right ear
contributions based on the distance and angle between the AudioListener and
the AudioSource. [More info](AudioSpatializerSDK.html)

#### Distortion Effect:

An **audio effect** Any effect that can modify the output of Audio Mixer
components, such as filtering frequency ranges of a sound or applying reverb.
[More info](class-AudioEffectMixer.html)  
See in [Glossary](Glossary.html#AudioEffect) that modifies the sound by
squashing and clipping the waveform to produce a rough, harsh result. [More
info](class-AudioDistortionFilter.html)

#### Doppler Factor:

An audio setting that allows you to control how much the velocity of an object
(relative to the audio listener) affects the pitch of any **audio sources** A
component which plays back an Audio Clip in the scene to an audio listener or
through an audio mixer. [More info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource) attached to it. [More
info](class-AudioManager.html)

#### Dry Level:

An audio setting that allows you to set the mix level of unprocessed signal in
output in mB.

#### Dry Mix:

An audio setting that allows you to set the volume of the original signal to
pass to output.

#### FMOD:

Audio in Unity is built on top of a middleware called FMOD. FMOD is integrated
with the Unity engine for creating and playing back interactive audio.

#### Play On Awake:

Set this to true to make an **Audio Source** A component which plays back an
Audio Clip in the scene to an audio listener or through an audio mixer. [More
info](class-AudioSource.html)  
See in [Glossary](Glossary.html#AudioSource) start playing on awake [More
info](class-AudioClip.html)

## Core terms

#### build:

The process of compiling your project into a format that is ready to run on a
specific platform or platforms. [More info](BuildSettings.html)

#### Managed plug-in:

A managed .NET assembly that is created with tools like Visual Studio for use
in Unity. [More info](./plug-ins.html)

#### Native plug-in:

A platform-specific native code library that is created outside of Unity for
use in Unity. Allows you can access features like OS calls and third-party
code libraries that would otherwise not be available to Unity. [More
info](./plug-ins.html)

#### Perforce:

A **version control** A system for managing file changes. You can use Unity in
conjunction with most common version control tools, including Perforce, Git,
Mercurial and PlasticSCM. [More info](VersionControl.html)  
See in [Glossary](Glossary.html#VersionControl) system for file change
management. [More info](perForceIntegration.html)

#### Development Build:

A **development build** A development build includes debug symbols and enables
the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-
target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](Glossary.html#DevelopmentBuild) includes debug symbols and
enables the **Profiler** A window that helps you to optimize your game. It
shows how much time is spent in the various areas of your game. For example,
it can report the percentage of time spent rendering, animating, or in your
game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler). [More
info](https://docs.unity.com/devops/en/manual/build-target-
configurations#Build_target_advanced_settings_overview)

## Editor terms

#### Anchor:

A **UI**(User Interface) Allows a user to interact with your application.
Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) layout tool that fixes a **UI** element to
a parent element. Anchors are shown as four small triangular handles in the
**Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view and anchor information is also
shown in the **Inspector** A Unity window that displays information about the
currently selected GameObject, asset or project settings, allowing you to
inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector). [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/UIBasicLayout.html#anchors)

#### Console window:

A Unity Editor window that shows errors, warnings and other messages generated
by Unity, or your own **scripts** A piece of code that allows you to create
your own Components, trigger game events, modify Component properties over
time and respond to user input in any way you like. [More info](creating-
scripts.html)  
See in [Glossary](Glossary.html#Scripts). [More info](Console.html)

#### Build profile:

A set of customizable configuration settings to use when creating a build for
your target platform. [More info](build-profiles.html)

#### Flythrough mode:

A **Scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view navigation mode that allows you to
fly around the **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) in first-person, similar to how you
would navigate in many games. [More info](SceneViewNavigation.html#flythrough)

#### Input Manager:

Settings where you can define all the different input axes, buttons and
controls for your project. [More info](class-InputManager.html)

#### Inspector:

A Unity window that displays information about the currently selected
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject), asset or **project settings** A
broad collection of settings which allow you to configure how Physics, Audio,
Networking, Graphics, Input and many other areas of your project behave. [More
info](comp-ManagerGroup.html)  
See in [Glossary](Glossary.html#ProjectSettings), allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)

#### Player Settings:

Settings that let you set various player-specific options for the final game
built by Unity. [More info](class-PlayerSettings.html)

#### Project window:

A window that shows the contents of your `Assets` folder (Project tab) [More
info](ProjectView.html)

#### Property Drawer:

A Unity feature that allows you to customize the look of certain controls in
the **Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window by using attributes on your
**scripts** A piece of code that allows you to create your own Components,
trigger game events, modify Component properties over time and respond to user
input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), or by controlling how a specific
Serializable class should look [More info](editor-PropertyDrawers.html)

#### Scene View:

An interactive view into the world you are creating. You use the **Scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) View to select and position scenery,
characters, **cameras** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera), lights, and all other types of Game
Object. [More info](UsingTheSceneView.html)

#### Time Manager:

A Unity Settings Manager that lets you set a number of properties that control
timing within your game. [More info](class-TimeManager.html)

#### zoom:

A **camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) control that lets you scale the view
on your screen. To zoom a **camera** in the Unity Editor, press Alt + right
click and drag. [More info](SceneViewNavigation.html)

## General terms

#### Animation Key:

The value of an animatable property, set at a specific point in time. Setting
at least two keys for the same property creates an animation. [More
info](animeditor-AnimationCurves.html)

#### category:

A **Profiler** A window that helps you to optimize your game. It shows how
much time is spent in the various areas of your game. For example, it can
report the percentage of time spent rendering, animating, or in your game
logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) category identifies the workload
data for a Unity subsystem (for example, Rendering, Scripting and Animation
categories). Unity applies colour-coding to categories to help visually
distinguish the types of data in the **Profiler** window. [More
info](ProfilerWindow.html)

#### compression:

A method of storing data that reduces the amount of storage space it requires.
See [Texture Compression](class-TextureImporterOverride)3D Graphics hardware
requires Textures to be compressed in specialized formats which are optimized
for fast Texture sampling. [More info](class-TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureCompression), [Animation
Compression](class-AnimationClip.html#AssetProperties)The method of
compressing animation data to significantly reduce file sizes without causing
a noticeable reduction in motion quality. Animation compression is a trade off
between saving on memory and image quality. [More info](class-
AnimationClip.html#AssetProperties)  
See in [Glossary](Glossary.html#animationcompression), [Audio
Compression](class-AudioClip.html), [Build
Compression](ReducingFilesize.html).

#### console:

Abbreviation of **game console** A device that runs and displays video games.  
See in [Glossary](Glossary.html#gameconsole)

#### Deferred shading:

A **rendering path** The technique that a render pipeline uses to render
graphics. Choosing a different rendering path affects how lighting and shading
are calculated. Some rendering paths are more suited to different platforms
and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) in the Built-in **Render
Pipeline** A series of operations that take the contents of a Scene, and
displays them on a screen. Unity lets you choose from pre-built render
pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) that places no limit on the
number of Lights that can affect a **GameObject** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). All Lights are evaluated per-
pixel, which means that they all interact correctly with **normal maps** A
type of Bump Map texture that allows you to add surface detail such as bumps,
grooves, and scratches to a model which catch the light as if they are
represented by real geometry.  
See in [Glossary](Glossary.html#Normalmap) and so on. Additionally, all Lights
can have cookies and shadows. [More info](RenderTech-DeferredShading.html)

#### Extrapolate:

See **Extrapolation** The process of storing the last few known values and
using them to predict future values. Used in animation, physics and
multiplayer.  
See in [Glossary](Glossary.html#Extrapolation)

#### Extrapolation:

The process of storing the last few known values and using them to predict
future values. Used in animation, physics and multiplayer.

#### first person shooter:

A common game genre, featuring a first-person view of a 3D world, and gun-
based combat with other players or NPCs.

#### FBX:

Autodesk’s proprietary format that Unity uses to import and export Models,
animation, and more. [More info](ImportingAssets.html)

#### FPS:

See **first person shooter** A common game genre, featuring a first-person
view of a 3D world, and gun-based combat with other players or NPCs.  
See in [Glossary](Glossary.html#firstpersonshooter), **frames per second** The
frequency at which consecutive frames are displayed in a running game. [More
info](RenderingStatistics.html)  
See in [Glossary](Glossary.html#framespersecond).

#### game console:

A device that runs and displays video games.

#### game controller:

A device to control objects and characters in a game.

#### GameObject:

The fundamental object in Unity **scenes** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), which can represent characters, props,
scenery, **cameras** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera), waypoints, and more. A **GameObject**
The fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject)’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)

#### Ignore file:

A special file used in many **Version Control** A system for managing file
changes. You can use Unity in conjunction with most common version control
tools, including Perforce, Git, Mercurial and PlasticSCM. [More
info](VersionControl.html)  
See in [Glossary](Glossary.html#VersionControl) Systems which specifies files
to be excluded from being placed under **version control** A system for
managing file changes. You can use Unity in conjunction with most common
version control tools, including Perforce, Git, Mercurial and PlasticSCM.
[More info](VersionControl.html)  
See in [Glossary](Glossary.html#VersionControl). In Unity projects there are a
number of files which could be excluded from **version control** , and using
an Ignore File is the best way to achieve this.

#### Input Key:

A key on a keyboard relating to the Input class. [More
info](../ScriptReference/KeyCode.html)

#### Interpolate:

See **Interpolation** The process of calculating values in-between two defined
values. Used in animation (between keyframes), physics (between physics time-
steps), and multiplayer (between network updates)  
See in [Glossary](Glossary.html#Interpolation)

#### Interpolation:

The process of calculating values in-between two defined values. Used in
animation (between keyframes), physics (between physics time-steps), and
multiplayer (between network updates)

#### Joy Num:

An **Input Manager** Settings where you can define all the different input
axes, buttons and controls for your project. [More info](class-
InputManager.html)  
See in [Glossary](Glossary.html#InputManager) property that defines which
joystick will be used. [More info](class-InputManager.html)

#### Layer Mask:

A value defining which layers to include or exclude from an operation, such as
rendering, **collision** A collision occurs when the physics engine detects
that the colliders of two GameObjects make contact or overlap, when at least
one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) or your own code. [More
info](Layers.html)

#### marker:

A Unity **Profiler** A window that helps you to optimize your game. It shows
how much time is spent in the various areas of your game. For example, it can
report the percentage of time spent rendering, animating, or in your game
logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) API structure that describes a CPU
or GPU event, such as a button click. Each event marker appears as a vertical
lines or label in the **Profiler** window. [More info](profiler-markers.html)

#### Mask:

Can refer to a **Sprite** A 2D graphic objects. If you are used to working in
3D, Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) Mask, a **UI**(User Interface) Allows
a user to interact with your application. Unity currently supports three UI
systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Mask, or a **Layer Mask** A value defining
which layers to include or exclude from an operation, such as rendering,
collision or your own code. [More info](Layers.html)  
See in [Glossary](Glossary.html#LayerMask) [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-
Mask.html)

#### Object:

See **GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

#### Packages:

Packages are collections of assets to be shared and re-used in Unity. The
[Unity Package Manager](upm-ui.html) (UPM) can display, add, and remove
packages from your project. These packages are native to the Unity Package
Manager and provide a fundamental method of delivering Unity functionality.
However, the Unity Package Manager can also display [Asset Store
packages](AssetStorePackages.html) that you downloaded from the **Asset
Store** A growing library of free and commercial assets created by Unity and
members of the community. Offers a wide variety of assets, from textures,
models and animations to whole project examples, tutorials and Editor
extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore). [More info](Packages.html)

#### Parent:

An object that contains child objects in a hierarchy. When a **GameObject**
The fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) is a Parent of another
**GameObject** , the Child **GameObject** will move, rotate, and scale exactly
as its Parent does. You can think of parenting as being like the relationship
between your arms and your body; whenever your body moves, your arms also move
along with it. [More info](class-Transform.html#parent)

#### Profiler:

A window that helps you to optimize your game. It shows how much time is spent
in the various areas of your game. For example, it can report the percentage
of time spent rendering, animating or in your game logic. [More
info](Profiler.html)

#### Project:

In Unity, you use a project to design and develop a game. A project stores all
of the files that are related to a game, such as the asset and **Scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) files. [More info](2Dor3D.html)

#### Project Settings:

A broad collection of settings which allow you to configure how Physics,
Audio, **Networking** The Unity system that enables multiplayer gaming across
a computer network. [More info](multiplayer.html)  
See in [Glossary](Glossary.html#Networking), Graphics, Input and many other
areas of your project behave. [More info](comp-ManagerGroup.html)

#### Plug-in:

A set of code created outside of Unity that creates functionality in Unity.
There are two kinds of **plug-ins** A set of code created outside of Unity
that creates functionality in Unity. There are two kinds of plug-ins you can
use in Unity: Managed plug-ins (managed .NET assemblies created with tools
like Visual Studio) and Native plug-ins (platform-specific native code
libraries). [More info](./plug-ins.html)  
See in [Glossary](Glossary.html#Plug-in) you can use in Unity: Managed **plug-
ins** (managed .NET assemblies created with tools like Visual Studio) and
Native **plug-ins** (platform-specific native code libraries). [More
info](./plug-ins.html)

#### Sprite Mask:

A texture which defines which areas of an underlying image to reveal or hide.
[More info](sprite/mask/mask-landing.html)

#### Transform Component:

A **Transform component** A Transform component determines the Position,
Rotation, and Scale of each object in the scene. Every GameObject has a
Transform. [More info](class-Transform.html)  
See in [Glossary](Glossary.html#TransformComponent) determines the Position,
Rotation, and Scale of each object in the **scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). Every **GameObject** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) has a Transform. [More
info](class-Transform.html)

#### Tree:

A **GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) and associated Component that
allows you to add tree assets to your **Scene** A Scene contains the
environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). You can add branch levels and leaves
to trees in the Tree **Inspector** A Unity window that displays information
about the currently selected GameObject, asset or project settings, allowing
you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window. [More info](class-
Tree.html)

#### Velocity:

A vector that defines the speed and direction of motion of a Rigidbody

#### VSync:

Vertical synchronization (VSync) is a display setting that caps a game’s frame
rate to match the refresh rate of a monitor, to prevent image tearing. [More
info](https://en.wikipedia.org/wiki/Screen_tearing#V-sync)

#### Version Control:

A system for managing file changes. You can use Unity in conjunction with most
common **version control** A system for managing file changes. You can use
Unity in conjunction with most common version control tools, including
Perforce, Git, Mercurial and PlasticSCM. [More info](VersionControl.html)  
See in [Glossary](Glossary.html#VersionControl) tools, including **Perforce**
A version control system for file change management. [More
info](perForceIntegration.html)  
See in [Glossary](Glossary.html#Perforce), Git, Mercurial and PlasticSCM.
[More info](VersionControl.html)

#### Viewport:

The user’s visible area of an app on their screen.

#### World:

The area in your **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) in which all objects reside. Often used
to specify that coordinates are world-relative, as opposed to object-relative.

## Graphics terms

#### Ambient light:

Light that doesn’t come from any specific direction, and contributes equal
light in all directions to the **Scene** A Scene contains the environments and
menus of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). [More info](lighting-window.html)

#### Ambient occlusion:

A method to approximate how much **ambient light** Light that doesn’t come
from any specific direction, and contributes equal light in all directions to
the Scene. [More info](lighting-window.html)  
See in [Glossary](Glossary.html#Ambientlight) (light not coming from a
specific direction) can hit a point on a surface.

#### Aniso Level:

The anisotropic filtering (AF) level of a texture. Allows you to increase
texture quality when viewing a texture at a steep angle. Good for floor and
ground textures. [More info](class-TextureImporter.html)

#### Antialiasing:

A technique for decreasing artifacts, like jagged lines (jaggies), in images
to make them appear smoother.

#### Aspect Ratio:

The relationship of an image’s proportional dimensions, such as its width and
height.

#### Baked Lights:

Light components whose Mode property is set to Baked. Unity pre-calculates the
illumination from **Baked Lights** Light components whose Mode property is set
to Baked. Unity pre-calculates the illumination from Baked Lights before
runtime, and does not include them in any runtime lighting calculations. [More
info](LightModes-introduction.html#baked)  
See in [Glossary](Glossary.html#BakedLights) before runtime, and does not
include them in any runtime lighting calculations. [More info](LightModes-
introduction.html#baked)

#### Billboard:

A textured **2D object** A 2D GameObject such as a tilemap or sprite. [More
info](Unity2D.html)  
See in [Glossary](Glossary.html#2DObject) that rotates so that it always faces
the **Camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). [More info](class-
BillboardRenderer.html)

#### blit:

A shorthand term for “bit block transfer”. A **blit** A shorthand term for
“bit block transfer”. A blit operation is the process of transferring blocks
of data from one place in memory to another.  
See in [Glossary](Glossary.html#blit) operation is the process of transferring
blocks of data from one place in memory to another.

#### Bloom:

A **post-processing** A process that improves product visuals by applying
filters and effects before the image appears on screen. You can use post-
processing effects to simulate physical camera and film properties, for
example Bloom and Depth of Field. [More info](PostProcessingOverview.html)
post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) effect used to reproduce an
imaging artifact of real-world **cameras** A component which creates an image
of a particular viewpoint in your scene. The output is either drawn to the
screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). The effect produces fringes of light
extending from the borders of bright areas in an image, contributing to the
illusion of an extremely bright light overwhelming the **camera** A component
which creates an image of a particular viewpoint in your scene. The output is
either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) or eye capturing the **scene** A Scene
contains the environments and menus of your game. Think of each unique Scene
file as a unique level. In each Scene, you place your environments, obstacles,
and decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

#### Bump map:

An image texture used to represent geometric detail across the surface of a
**mesh** The main graphics primitive of Unity. Meshes make up a large part of
your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes.
Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh), for example bumps and grooves. Can be
represented as a **heightmap** A greyscale Texture that stores height data for
an object. Each pixel stores the height difference perpendicular to the face
that pixel represents.  
See in [Glossary](Glossary.html#Heightmap) or a **normal map** A type of Bump
Map texture that allows you to add surface detail such as bumps, grooves, and
scratches to a model which catch the light as if they are represented by real
geometry.  
See in [Glossary](Glossary.html#Normalmap). [More
info](StandardShaderMaterialParameterNormalMap.html)

#### Camera:

A component which creates an image of a particular viewpoint in your **scene**
A Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). The output is either drawn to the
screen or captured as a texture. [More info](CamerasOverview.html)

#### clipping plane:

A plane that limits how far or close a **camera** A component which creates an
image of a particular viewpoint in your scene. The output is either drawn to
the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) can see from its current position. A
**camera** ’s viewable range is between the far and near **clipping planes** A
plane that limits how far or close a camera can see from its current position.
A camera’s viewable range is between the far and near clipping planes. See far
clipping plane and near clipping plane. [More info](class-Camera.html)  
See in [Glossary](Glossary.html#clippingplane). See far **clipping plane** A
plane that limits how far or close a camera can see from its current position.
A camera’s viewable range is between the far and near clipping planes. See far
clipping plane and near clipping plane. [More info](class-Camera.html)  
See in [Glossary](Glossary.html#clippingplane) and near **clipping plane**.
[More info](class-Camera.html)

#### component:

A functional part of a **GameObject** The fundamental object in Unity scenes,
which can represent characters, props, scenery, cameras, waypoints, and more.
A GameObject’s functionality is defined by the Components attached to it.
[More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). A **GameObject** can contain any
number of components. Unity has many built-in components, and you can create
your own by writing **scripts** A piece of code that allows you to create your
own Components, trigger game events, modify Component properties over time and
respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) that inherit from MonoBehaviour.
[More info](UsingComponents.html)

#### Cubemap:

A collection of six square textures that can represent the reflections in an
environment or the **skybox** A special type of Material used to represent
skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) drawn behind your geometry. The six
squares form the faces of an imaginary cube that surrounds an object; each
face represents the view along the directions of the world axes (up, down,
left, right, forward and back). [More info](class-Cubemap-landing.html)

#### Culling Mask:

Allows you to include or omit objects to be rendered by a **Camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera), by Layer.

#### depth buffer:

A memory store that holds the z-value depth of each **pixel** The smallest
unit in a computer image. Pixel size depends on your screen resolution. Pixel
lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) in an image, where the z-value is the
depth for each rendered **pixel** from the projection plane. [More
info](class-RenderTexture.html)

#### Depth of Field:

A **post-processing** A process that improves product visuals by applying
filters and effects before the image appears on screen. You can use post-
processing effects to simulate physical camera and film properties, for
example Bloom and Depth of Field. [More info](PostProcessingOverview.html)
post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) effect that simulates the
focus properties of a **camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) lens. [More
info](PostProcessingOverview.html)

#### Distance Shadowmask:

A version of the **Shadowmask** A Texture that shares the same UV layout and
resolution with its corresponding lightmap. [More info](lighting-
mode.html#shadowmask)  
See in [Glossary](Glossary.html#Shadowmask) lighting mode that includes high
quality shadows cast from static **GameObjects** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) onto dynamic **GameObjects**.
[More info](lighting-mode.html#shadowmask)

#### Dynamic Batching:

An automatic Unity process which attempts to render multiple meshes as if they
were a single **mesh** The main graphics primitive of Unity. Meshes make up a
large part of your 3D worlds. Unity supports triangulated or Quadrangulated
polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
[More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) for optimized graphics performance. The
technique transforms all of the **GameObject** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) vertices on the CPU and groups
many similar vertices together. [More info](DrawCallBatching.html)

#### dynamic resolution:

A **Camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) setting that allows you to dynamically
scale individual render targets to reduce workload on the GPU. [More
info](DynamicResolution-landing.html)

#### Enlighten:

A lighting system by Geomerics used in Unity for **Enlighten** A lighting
system by Geomerics used in Unity for Enlighten Realtime Global Illumination.
[More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime **Global Illumination** A
group of techniques that model both direct and indirect lighting to provide
realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination). [More
info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)

#### ETC:

(Ericsson Texture Compression) A block-based **texture format** A file format
for handling textures during real-time rendering by 3D graphics hardware, such
as a graphics card or mobile device. [More info](class-
TextureImporterOverride)  
See in [Glossary](Glossary.html#TextureFormat) that compresses textures to
significantly reduce file sizes without causing a noticable reduction in image
quality. [More info](class-TextureImporterOverride)

#### Exponential fog:

A fog model that emulates realistic fog behaviour by simulating light
absorption over distance by a certain attenuation factor.

#### Exposure value:

A value that represents a combination of a **camera** A component which
creates an image of a particular viewpoint in your scene. The output is either
drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera)’s shutter speed and f-number. It is
essentially a measurement of exposure such that all combinations of shutter
speed and f-number that yield the same level of exposure have the same EV.

#### Extrude Edges:

A Texture property that enables you to define how much area to leave around a
**sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are
essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) in a generated **mesh** The main
graphics primitive of Unity. Meshes make up a large part of your 3D worlds.
Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms,
Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh).

#### Far clipping plane:

The maximum draw distance for a **camera** A component which creates an image
of a particular viewpoint in your scene. The output is either drawn to the
screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). Geometry beyond the plane defined by
this value is not rendered. The plane is perpendicular to the **camera** ’s
forward (Z) direction.

#### Fog:

A **post-processing** A process that improves product visuals by applying
filters and effects before the image appears on screen. You can use post-
processing effects to simulate physical camera and film properties, for
example Bloom and Depth of Field. [More info](PostProcessingOverview.html)
post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) effect that overlays a color
onto objects depending on the distance from the **camera** A component which
creates an image of a particular viewpoint in your scene. The output is either
drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). Use this to simulate fog or mist in
outdoor environments, or to hide clipping of objects near the **camera** ’s
far clip plane. [More info](PostProcessingOverview.html)

#### Forward Rendering:

A **rendering path** The technique that a render pipeline uses to render
graphics. Choosing a different rendering path affects how lighting and shading
are calculated. Some rendering paths are more suited to different platforms
and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) that renders each object in one
or more passes, depending on lights that affect the object. Lights themselves
are also treated differently by **Forward Rendering** A rendering path that
renders each object in one or more passes, depending on lights that affect the
object. Lights themselves are also treated differently by Forward Rendering,
depending on their settings and intensity. [More info](RenderTech-
ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering), depending on their settings
and intensity. [More info](RenderTech-ForwardRendering.html)

#### frame:

A single image from a sequence of images that represent moving graphics. While
your game is running, the **camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) in your game renders frames to the
screen as fast as possible. May also refer to a frame from a video clip, or
**sprite** A 2D graphic objects. If you are used to working in 3D, Sprites are
essentially just standard textures but there are special techniques for
combining and managing sprite textures for efficiency and convenience during
development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) animation frames. See **frames per
second** The frequency at which consecutive frames are displayed in a running
game. [More info](RenderingStatistics.html)  
See in [Glossary](Glossary.html#framespersecond) (FPS).

#### frames per second:

The frequency at which consecutive frames are displayed in a running game.
[More info](RenderingStatistics.html)

#### Fresnel Effect:

An effect representing the increase in reflectivity on objects when light hits
at grazing angles.

#### Frustum:

The region of 3D space that a perspective **camera** A component which creates
an image of a particular viewpoint in your scene. The output is either drawn
to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) can see and render. In the **Scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) view, the frustum is represented by a
truncated rectangular pyramid with its top at the **camera__’s near** clipping
plane__A plane that limits how far or close a camera can see from its current
position. A camera’s viewable range is between the far and near clipping
planes. See far clipping plane and near clipping plane. [More info](class-
Camera.html)  
See in [Glossary](Glossary.html#clippingplane) and its base at the
**camera__’s far** clipping plane__. [More info](UnderstandingFrustum.html)

#### GI Cache:

The cached intermediate files used when Unity precomputes lighting data. Unity
keeps this cache to speed up computation. [More info](GICache.html)

#### Gizmo:

A graphic overlay associated with a **GameObject** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in a **Scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), and displayed in the **Scene** View.
Built-in **scene** A Scene contains the environments and menus of your game.
Think of each unique Scene file as a unique level. In each Scene, you place
your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) tools such as the move tool are
**Gizmos** A graphic overlay associated with a GameObject in a Scene, and
displayed in the Scene View. Built-in scene tools such as the move tool are
Gizmos, and you can create custom Gizmos using textures or scripting. Some
Gizmos are only drawn when the GameObject is selected, while other Gizmos are
drawn by the Editor regardless of which GameObjects are selected. [More
info](GizmosMenu.html#GizmosIcons)  
See in [Glossary](Glossary.html#Gizmo), and you can create custom **Gizmos**
using textures or scripting. Some **Gizmos** are only drawn when the
**GameObject** is selected, while other **Gizmos** are drawn by the Editor
regardless of which **GameObjects** The fundamental object in Unity scenes,
which can represent characters, props, scenery, cameras, waypoints, and more.
A GameObject’s functionality is defined by the Components attached to it.
[More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) are selected. [More
info](GizmosMenu.html#GizmosIcons)

#### global illumination:

A group of techniques that model both direct and indirect lighting to provide
realistic lighting results.

#### Gravity Modifier:

A **Particle System** A component that simulates fluid entities such as
liquids, clouds and flames by generating and animating large numbers of small
2D images in the scene. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem) property that scales the
gravity value set in the physics manager. A value of zero switches gravity
off. [More info](PartSysMainModule.html)

#### Halo:

The glowing light areas around light sources, used to give the impression of
small dust particles in the air. [More info](class-Halo.html)

#### Hard Shadows:

A shadow property that produces shadows with a sharp edge. Hard shadows are
not particularly realistic compared to Soft Shadows but they involve less
processing, and are acceptable for many purposes.

#### HDR:

high dynamic range

#### HDRI:

high dynamic range image

#### Heightmap:

A greyscale Texture that stores height data for an object. Each **pixel** The
smallest unit in a computer image. Pixel size depends on your screen
resolution. Pixel lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) stores the height difference
perpendicular to the face that **pixel** represents.

#### Irradiance Budget:

A **lightmap** A pre-rendered texture that contains the effects of light
sources on static objects in the scene. Lightmaps are overlaid on top of scene
geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) property that determines the
precision of the incoming light data used to light each texel in the
**lightmap** [More info](class-LightmapParameters.html)

#### Irradiance Quality:

A **lightmap** A pre-rendered texture that contains the effects of light
sources on static objects in the scene. Lightmaps are overlaid on top of scene
geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) property that sets the number of
rays that are cast and used to compute which clusters affect a given output
**lightmap** texel. [More info](class-LightmapParameters.html)

#### Layer:

Layers in Unity can be used to selectively opt groups of **GameObjects** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in or out of certain processes or
calculations. This includes **camera** A component which creates an image of a
particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) rendering, lighting, physics
**collisions** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision), or custom calculations in your own
code. [More info](Layers.html)

#### Lens Flare:

A component that simulates the effect of lights refracting inside a **camera**
A component which creates an image of a particular viewpoint in your scene.
The output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) lens. Use a **Lens Flare** A component
that simulates the effect of lights refracting inside a camera lens. Use a
Lens Flare to represent very bright lights or add atmosphere to your scene.
[More info](class-LensFlare.html)  
See in [Glossary](Glossary.html#LensFlare) to represent very bright lights or
add atmosphere to your **scene** A Scene contains the environments and menus
of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). [More info](class-LensFlare.html)

#### level of detail:

The _Level Of Detail_ (LOD) technique is an optimization that reduces the
number of triangles that Unity has to render for a **GameObject** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) when its distance from the
**Camera** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) increases. [More
info](LevelOfDetail.html)

#### Light Mode:

A Light property that defines the use of the Light. Can be set to Realtime,
Baked and Mixed. [More info](LightModes.html)

#### Light Probe:

Light probes store information about how light passes through space in your
**scene** A Scene contains the environments and menus of your game. Think of
each unique Scene file as a unique level. In each Scene, you place your
environments, obstacles, and decorations, essentially designing and building
your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). A collection of **light probes** Light
probes store information about how light passes through space in your scene. A
collection of light probes arranged within a given space can improve lighting
on moving objects and static LOD scenery within that space. [More
info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) arranged within a given space can
improve lighting on moving objects and static **LOD** The _Level Of Detail_
(LOD) technique is an optimization that reduces the number of triangles that
Unity has to render for a GameObject when its distance from the Camera
increases. [More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#LOD) scenery within that space. [More
info](LightProbes.html)

#### Light Probe Group:

A component that enables you to add **Light Probes** Light probes store
information about how light passes through space in your scene. A collection
of light probes arranged within a given space can improve lighting on moving
objects and static LOD scenery within that space. [More
info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) to **GameObjects** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in your **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). [More info](class-
LightProbeGroup.html)

#### Light Probe Proxy Volume:

A component that allows you to use more lighting information for large dynamic
**GameObjects** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that cannot use baked
**lightmaps** A pre-rendered texture that contains the effects of light
sources on static objects in the scene. Lightmaps are overlaid on top of scene
geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) (for example, large Particle Systems
or skinned Meshes). [More info](class-LightProbeProxyVolume.html)

#### Lightmap:

A pre-rendered texture that contains the effects of light sources on static
objects in the **scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). **Lightmaps** A pre-rendered texture
that contains the effects of light sources on static objects in the scene.
Lightmaps are overlaid on top of scene geometry to create the effect of
lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) are overlaid on top of **scene**
geometry to create the effect of lighting. [More info](Lightmapping.html)

#### Lightmapper:

A tool in Unity that bakes **lightmaps** A pre-rendered texture that contains
the effects of light sources on static objects in the scene. Lightmaps are
overlaid on top of scene geometry to create the effect of lighting. [More
info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) according to the arrangement of
lights and geometry in your **scene** A Scene contains the environments and
menus of your game. Think of each unique Scene file as a unique level. In each
Scene, you place your environments, obstacles, and decorations, essentially
designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). [More info](Lightmapping.html)

#### Line Renderer:

A component that takes an array of two or more points in 3D space and draws a
straight line between each one. You can use a single **Line Renderer** A
component that takes an array of two or more points in 3D space and draws a
straight line between each one. You can use a single Line Renderer component
to draw anything from a simple straight line to a complex spiral. [More
info](class-LineRenderer.html)  
See in [Glossary](Glossary.html#LineRenderer) component to draw anything from
a simple straight line to a complex spiral. [More info](class-
LineRenderer.html)

#### LOD:

See **level of detail** The _Level Of Detail_ (LOD) technique is an
optimization that reduces the number of triangles that Unity has to render for
a GameObject when its distance from the Camera increases. [More
info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#levelofdetail)

#### LOD Group:

A component to manage **level of detail** The _Level Of Detail_ (LOD)
technique is an optimization that reduces the number of triangles that Unity
has to render for a GameObject when its distance from the Camera increases.
[More info](LevelOfDetail.html)  
See in [Glossary](Glossary.html#levelofdetail) (LOD) for **GameObjects** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject). [More info](class-LODGroup.html)

#### Material:

An asset that defines how a surface should be rendered. [More info](class-
Material.html)

#### Mesh:

The main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)

#### Mesh Filter:

A **mesh** The main graphics primitive of Unity. Meshes make up a large part
of your 3D worlds. Unity supports triangulated or Quadrangulated polygon
meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) component that takes a **mesh** from
your assets and passes it to the **Mesh** The main graphics primitive of
Unity. Meshes make up a large part of your 3D worlds. Unity supports
triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces
must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderer for rendering on the screen.
[More info](class-MeshFilter.html)

#### Mesh Renderer:

A **mesh** The main graphics primitive of Unity. Meshes make up a large part
of your 3D worlds. Unity supports triangulated or Quadrangulated polygon
meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) component that takes the geometry from
the **Mesh** The main graphics primitive of Unity. Meshes make up a large part
of your 3D worlds. Unity supports triangulated or Quadrangulated polygon
meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Filter and renders it at the position
defined by the object’s **Transform component** A Transform component
determines the Position, Rotation, and Scale of each object in the scene.
Every GameObject has a Transform. [More info](class-Transform.html)  
See in [Glossary](Glossary.html#TransformComponent). [More info](class-
MeshRenderer.html)

#### Near clipping plane:

A plane that limits how close a **camera** A component which creates an image
of a particular viewpoint in your scene. The output is either drawn to the
screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) can see from its current position. The
plane is perpendicular to the **camera** ’s forward (Z) direction. [More
info](CamerasOverview.html)

#### Normal:

The direction perpendicular to the surface of a **mesh** The main graphics
primitive of Unity. Meshes make up a large part of your 3D worlds. Unity
supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv
surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh), represented by a Vector. Unity uses
normals to determine object orientation and apply shading. [More
info](scripting-vectors.html)

#### Normal map:

A type of **Bump Map** An image texture used to represent geometric detail
across the surface of a mesh, for example bumps and grooves. Can be
represented as a heightmap or a normal map. [More
info](StandardShaderMaterialParameterNormalMap.html)  
See in [Glossary](Glossary.html#Bumpmap) texture that allows you to add
surface detail such as bumps, grooves, and scratches to a model which catch
the light as if they are represented by real geometry.

#### Occlusion culling:

A process that disables rendering **GameObjects** The fundamental object in
Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that are hidden (occluded) from
the view of the **camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). [More info](OcclusionCulling.html)

#### Orthographic 3D:

A common type of **camera** A component which creates an image of a particular
viewpoint in your scene. The output is either drawn to the screen or captured
as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) view used in games that give you a
bird’s-eye view of the action, and is sometimes called “2.5D”. [More
info](2Dor3D.html)

#### particle:

A small, simple image or **mesh** The main graphics primitive of Unity. Meshes
make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) that is emitted by a **particle system**
A component that simulates fluid entities such as liquids, clouds and flames
by generating and animating large numbers of small 2D images in the scene.
[More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem). A **particle system** can
display and move particles in great numbers to represent a fluid or amorphous
entity. The effect of all the particles together creates the impression of the
complete entity, such as smoke. [More info](class-ParticleSystem.html)

#### particle system:

A component that simulates fluid entities such as liquids, clouds and flames
by generating and animating large numbers of small 2D images in the **scene**
A Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). [More info](class-ParticleSystem.html)

#### Physically Based Shading:

An advanced lighting model that simulates the interactions between materials
and light in a way that mimics reality. [More info](shader-
StandardShader.html)

#### pixel:

The smallest unit in a computer image. **Pixel** The smallest unit in a
computer image. Pixel size depends on your screen resolution. Pixel lighting
is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) size depends on your screen resolution.
**Pixel** lighting is calculated at every screen **pixel** The smallest unit
in a computer image. Pixel size depends on your screen resolution. Pixel
lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel). [More info](ShadowPerformance.html)

#### Player Log:

The .log file created by a Standalone Player that contains a record of events,
such as script execution times, the compiler version, and AssetImport time.
Log files can help diagnose problems. [More info](log-files.html#player)

#### post-processing:

A process that improves product visuals by applying filters and effects before
the image appears on screen. You can use post-processing effects to simulate
physical camera and film properties, for example Bloom and Depth of Field.
[More info](PostProcessingOverview.html) post processing, postprocessing,
postprocess

#### pseudo-depth:

A visual simulation of three-dimensional characteristics on a two-dimensional
object or environment. This effect is sometimes called “2.5D”. [More
info](tilemaps/work-with-tilemaps/isometric-tilemaps/isometric-tilemap-
landing.html)

#### Quad:

A primitive object that resembles a plane but its edges are only one unit
long, it uses only 4 vertices, and the surface is oriented in the XY plane of
the local coordinate space. [More info](PrimitiveObjects.html)

#### Quaternion:

Unity’s standard way of representing rotations as data. When writing code that
deals with rotations, you should usually use the **Quaternion** Unity’s
standard way of representing rotations as data. When writing code that deals
with rotations, you should usually use the Quaternion class and its methods.
[More info](QuaternionAndEulerRotationsInUnity.html)  
See in [Glossary](Glossary.html#Quaternion) class and its methods. [More
info](QuaternionAndEulerRotationsInUnity.html)

#### Rasterization:

The process of generating an image by calculating **pixels** The smallest unit
in a computer image. Pixel size depends on your screen resolution. Pixel
lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) for each polygon or triangle in the
geometry. This is an alternative to **ray tracing** The process of generating
an image by tracing out rays from the Camera through each pixel and recording
the color contribution at the hit point. This is an alternative to
rasterization. raytracing  
See in [Glossary](Glossary.html#Raytracing).

#### Ray tracing:

The process of generating an image by tracing out rays from the Camera through
each pixel and recording the color contribution at the hit point. This is an
alternative to rasterization. raytracing

#### Realtime Lights:

Light components whose Mode property is set to Realtime. Unity calculates and
updates the lighting of **Realtime Lights** Light components whose Mode
property is set to Realtime. Unity calculates and updates the lighting of
Realtime Lights every frame at runtime. No Realtime Lights are precomputed.
[More info](LightModes-introduction.html#realtime)  
See in [Glossary](Glossary.html#RealtimeLights) every frame at runtime. No
**Realtime Lights** are precomputed. [More info](LightModes-
introduction.html#realtime)

#### Reflection Probe:

A rendering component that captures a spherical view of its surroundings in
all directions, rather like a **camera** A component which creates an image of
a particular viewpoint in your scene. The output is either drawn to the screen
or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). The captured image is then stored as
a **Cubemap** A collection of six square textures that can represent the
reflections in an environment or the skybox drawn behind your geometry. The
six squares form the faces of an imaginary cube that surrounds an object; each
face represents the view along the directions of the world axes (up, down,
left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) that can be used by objects with
reflective materials. [More info](class-ReflectionProbe.html)

#### Render pipeline:

A series of operations that take the contents of a **Scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), and displays them on a screen. Unity
lets you choose from pre-built **render pipelines** A series of operations
that take the contents of a Scene, and displays them on a screen. Unity lets
you choose from pre-built render pipelines, or write your own. [More
info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline), or write your own. [More
info](render-pipelines.html)

#### Render Texture:

A special type of Texture that is created and updated at runtime. To use them,
first create a new **Render Texture** A special type of Texture that is
created and updated at runtime. To use them, first create a new Render Texture
and designate one of your Cameras to render into it. Then you can use the
Render Texture in a Material just like a regular Texture. [More info](class-
RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture) and designate one of your
**Cameras** A component which creates an image of a particular viewpoint in
your scene. The output is either drawn to the screen or captured as a texture.
[More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) to render into it. Then you can use
the **Render Texture** in a Material just like a regular Texture. [More
info](class-RenderTexture.html)

#### Rendering Path:

The technique that a **render pipeline** A series of operations that take the
contents of a Scene, and displays them on a screen. Unity lets you choose from
pre-built render pipelines, or write your own. [More info](render-
pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline) uses to render graphics.
Choosing a different **rendering path** The technique that a render pipeline
uses to render graphics. Choosing a different rendering path affects how
lighting and shading are calculated. Some rendering paths are more suited to
different platforms and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) affects how lighting and
shading are calculated. Some **rendering paths** The technique that a render
pipeline uses to render graphics. Choosing a different rendering path affects
how lighting and shading are calculated. Some rendering paths are more suited
to different platforms and hardware than others. [More
info](RenderingPaths.html)  
See in [Glossary](Glossary.html#RenderingPath) are more suited to different
platforms and hardware than others. [More info](RenderingPaths.html)

#### Shader:

A program that runs on the GPU. [More info](Shaders.html)

#### Shader object:

An instance of the **Shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) class, a **Shader** object is
container for **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) programs and GPU instructions, and
information that tells Unity how to use them. Use them with materials to
determine the appearance of your **scene** A Scene contains the environments
and menus of your game. Think of each unique Scene file as a unique level. In
each Scene, you place your environments, obstacles, and decorations,
essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). [More info](shader-objects.html)

#### Shader variant:

A verion of a **shader** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) program that Unity generates according
to a specific combination of **shader** keywords and their status. A
**Shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) object can contain multiple **shader**
variants. [More info](shader-variants.html)

#### ShaderLab:

Unity’s language for defining the structure of **Shader** A program that runs
on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) objects. [More info](SL-Shader.html)

#### Shadowmask:

A Texture that shares the same UV layout and resolution with its corresponding
**lightmap** A pre-rendered texture that contains the effects of light sources
on static objects in the scene. Lightmaps are overlaid on top of scene
geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap). [More info](lighting-
mode.html#shadowmask)

#### Skybox:

A special type of Material used to represent skies. Usually six-sided. [More
info](sky-landing.html)

#### Soft Shadows:

A shadow property that produces shadows with a soft edge. Soft shadows are
more realistic compared to Hard Shadows and tend to reduce the “blocky”
aliasing effect from the shadow map, but they require more processing.

#### Spatial Mapping:

The process of mapping real-world surfaces into the virtual world.

#### specular color:

The color of a specular highlight.

#### specular highlight

A bright spot of light that appears on the surface of shiny objects when
illuminated.

#### Sprite:

A 2D graphic objects. If you are used to working in 3D, **Sprites** A 2D
graphic objects. If you are used to working in 3D, Sprites are essentially
just standard textures but there are special techniques for combining and
managing sprite textures for efficiency and convenience during development.
[More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) are essentially just standard textures
but there are special techniques for combining and managing **sprite** A 2D
graphic objects. If you are used to working in 3D, Sprites are essentially
just standard textures but there are special techniques for combining and
managing sprite textures for efficiency and convenience during development.
[More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) textures for efficiency and
convenience during development. [More info](sprite/sprite-landing.html)

#### Sprite Atlas:

A utility that packs several **sprite** A 2D graphic objects. If you are used
to working in 3D, Sprites are essentially just standard textures but there are
special techniques for combining and managing sprite textures for efficiency
and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) textures tightly together within a
single texture known as an atlas. [More info](sprite/atlas/v2/v2-landing.html)

#### Sprite Renderer:

A component that lets you display images as **Sprites** A 2D graphic objects.
If you are used to working in 3D, Sprites are essentially just standard
textures but there are special techniques for combining and managing sprite
textures for efficiency and convenience during development. [More
info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) for use in both 2D and 3D **scenes** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). [More info](sprite/renderer/renderer-
landing.html)

#### Static Batching:

A technique Unity uses to draw **GameObjects** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) on the screen that combines static
(non-moving) **GameObjects** into big Meshes, and renders them in a faster
way. [More info](DrawCallBatching.html)

#### Static receiver:

A static **GameObject** The fundamental object in Unity scenes, which can
represent characters, props, scenery, cameras, waypoints, and more. A
GameObject’s functionality is defined by the Components attached to it. [More
info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that is receiving a shadow from
another static or dynamic **GameObject** [More info](StaticObjects.html)

#### stencil buffer:

A memory store that holds an 8-bit per-pixel value. In Unity, you can use a
**stencil buffer** A memory store that holds an 8-bit per-pixel value. In
Unity, you can use a stencil buffer to flag pixels, and then only render to
pixels that pass the stencil operation. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#stencilbuffer) to flag **pixels** The smallest
unit in a computer image. Pixel size depends on your screen resolution. Pixel
lighting is calculated at every screen pixel. [More
info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel), and then only render to **pixels**
that pass the stencil operation. [More info](class-RenderTexture.html)

#### Surface Shader:

A streamlined way of writing **shaders** A program that runs on the GPU. [More
info](Shaders.html)  
See in [Glossary](Glossary.html#Shader) for the Built-in **Render Pipeline** A
series of operations that take the contents of a Scene, and displays them on a
screen. Unity lets you choose from pre-built render pipelines, or write your
own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#Renderpipeline). [More info](SL-
SurfaceShaders.html)

#### Terrain:

The landscape in your **scene** A Scene contains the environments and menus of
your game. Think of each unique Scene file as a unique level. In each Scene,
you place your environments, obstacles, and decorations, essentially designing
and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). A **Terrain** The landscape in your
scene. A Terrain GameObject adds a large flat plane to your scene and you can
use the Terrain’s Inspector window to create a detailed landscape. [More
info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) **GameObject** The fundamental object
in Unity scenes, which can represent characters, props, scenery, cameras,
waypoints, and more. A GameObject’s functionality is defined by the Components
attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) adds a large flat plane to your
**scene** and you can use the **Terrain** ’s **Inspector** A Unity window that
displays information about the currently selected GameObject, asset or project
settings, allowing you to inspect and edit the values. [More
info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window to create a detailed
landscape. [More info](terrain-UsingTerrains.html)

#### Text Mesh:

A **Mesh** The main graphics primitive of Unity. Meshes make up a large part
of your 3D worlds. Unity supports triangulated or Quadrangulated polygon
meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More
info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) component that displays a Text string
[More info](class-TextMesh.html)

#### texture:

An image used when rendering a **GameObject** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), **Sprite** A 2D graphic objects.
If you are used to working in 3D, Sprites are essentially just standard
textures but there are special techniques for combining and managing sprite
textures for efficiency and convenience during development. [More
info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite), or **UI**(User Interface) Allows a
user to interact with your application. Unity currently supports three UI
systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) element. Textures are often applied to the
surface of a **mesh** The main graphics primitive of Unity. Meshes make up a
large part of your 3D worlds. Unity supports triangulated or Quadrangulated
polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons.
[More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) to give it visual detail. [More
info](class-TextureImporter.html)

#### Texture Compression:

3D Graphics hardware requires Textures to be compressed in specialized formats
which are optimized for fast Texture sampling. [More info](class-
TextureImporterOverride)

#### Texture Import Inspector:

An **Inspector** A Unity window that displays information about the currently
selected GameObject, asset or project settings, allowing you to inspect and
edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) that allows you to define how your
images are imported from your project’s `Assets` folder into the Unity Editor.
[More info](class-TextureImporter.html)

#### Texture Overrides:

Platform-specific settings that allow you to set the resolution, file size
with associated memory size requirements, **pixel** The smallest unit in a
computer image. Pixel size depends on your screen resolution. Pixel lighting
is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) dimensions, and quality of your
Textures for each target platform. [More info](class-TextureImporterOverride)

#### Tile:

A simple class that allows a **sprite** A 2D graphic objects. If you are used
to working in 3D, Sprites are essentially just standard textures but there are
special techniques for combining and managing sprite textures for efficiency
and convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite) to be rendered on a **Tilemap** A
GameObject that allows you to quickly create 2D levels using tiles and a grid
overlay. [More info](tilemaps/work-with-tilemaps/tilemap-reference.html)  
See in [Glossary](Glossary.html#Tilemap). [More info](tilemaps/tiles-for-
tilemaps/scriptable-tiles/scriptable-tiles-landing.html)

#### Tilemap:

A **GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that allows you to quickly create
2D levels using tiles and a grid overlay. [More info](tilemaps/work-with-
tilemaps/tilemap-reference.html)

#### Tonemapping:

The process of remapping **HDR** high dynamic range  
See in [Glossary](Glossary.html#HDR) values of an image into a range suitable
to be displayed on screen. [More info](PostProcessingOverview.html)

#### Trail Renderer:

A visual effect that lets you to make trails behind **GameObjects** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) in the **Scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) as they move. [More info](class-
TrailRenderer.html)

#### vector field:

A 3D texture, where each value represents a directional force that is applied
to particles as they move through the field. A vector field is created in 3D
animation software, such as Houdini. [More
info](https://en.wikipedia.org/wiki/Vector_field)

#### vertex shader:

A program that runs on each vertex of a 3D model when the model is being
rendered. [More info](writing-shader-writing-shader-programs-hlsl.html)

#### VideoCapture:

A Unity API that allows you to record videos directly to the file system in
the MP4 format. [More
info](../ScriptReference/Windows.WebCam.VideoCapture.html)

#### WebGL:

A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity
Web build option allows Unity to publish content as JavaScript programs which
use HTML5 technologies and the **WebGL** A JavaScript API that renders 2D and
3D graphics in a web browser. The Unity Web build option allows Unity to
publish content as JavaScript programs which use HTML5 technologies and the
WebGL rendering API to run Unity content in a web browser. [More
info](webgl.html)  
See in [Glossary](Glossary.html#WebGL) rendering API to run Unity content in a
web browser. [More info](webgl.html)

#### wind zone:

A **GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) that adds the effect of wind to
your **terrain** The landscape in your scene. A Terrain GameObject adds a
large flat plane to your scene and you can use the Terrain’s Inspector window
to create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain). For instance, Trees within a **wind
zone** A GameObject that adds the effect of wind to your terrain. For
instance, Trees within a wind zone will bend in a realistic animated fashion
and the wind itself will move in pulses to create natural patterns of movement
among the tree. [More info](class-WindZone.html)  
See in [Glossary](Glossary.html#windzone) will bend in a realistic animated
fashion and the wind itself will move in pulses to create natural patterns of
movement among the tree. [More info](class-WindZone.html)

## Lighting terms

#### Mixed Lights:

Light components whose Mode property is set to Mixed. Some calculations for
Mixed Lights are performed in advance, and some calculations for Mixed Lights
are performed at runtime. The behavior of all Mixed Lights in a **Scene** A
Scene contains the environments and menus of your game. Think of each unique
Scene file as a unique level. In each Scene, you place your environments,
obstacles, and decorations, essentially designing and building your game in
pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) is determined by the **Scene** ’s
Lighting Mode. [More info](LightModes-landing.html)

## Multiplayer terms

#### HLAPI:

Abbreviation of **High Level API**.

#### Host:

In a multiplayer network game without a dedicated server, one of the peers in
the game acts as the center of authority for the game. This peer is called the
“host”. It runs a server and a “local client”, while the other peers each run
a “remote client”. [More info](multiplayer.html)

#### Main Editor Player:

The Unity Player that exists in the main Unity Editor.

#### Networking:

The Unity system that enables multiplayer gaming across a computer network.
[More info](multiplayer.html)

#### Virtual Player:

A Unity Player that exists separately from the **main Editor Player** The
Unity Player that exists in the main Unity Editor.  
See in [Glossary](Glossary.html#MainEditorPlayer). Use a **Virtual Player** A
Unity Player that exists separately from the **main Editor Player**. Use a
Virtual Player to test multiplayer gameplay on the same device without the
need to create a build. [More info](https://docs-
multiplayer.unity3d.com/mppm/current/virtual-players/)  
See in [Glossary](Glossary.html#VirtualPlayer) to test multiplayer gameplay on
the same device without the need to create a build. [More info](https://docs-
multiplayer.unity3d.com/mppm/current/virtual-players/)

#### Tag:

A reference word that you can assign to a **Virtual Player** A Unity Player
that exists separately from the **main Editor Player**. Use a Virtual Player
to test multiplayer gameplay on the same device without the need to create a
build. [More info](https://docs-multiplayer.unity3d.com/mppm/current/virtual-
players/)  
See in [Glossary](Glossary.html#VirtualPlayer) or the **main Editor Player**
The Unity Player that exists in the main Unity Editor.  
See in [Glossary](Glossary.html#MainEditorPlayer) to use in a script. For
example, you could define a “Red team” ot “Blue team” tag to assign Players to
each team. [More info](https://docs-
multiplayer.unity3d.com/mppm/current/player-tags/)

## Package Manager terms

#### Built-in package:

_Built-in_ packages allow users to toggle Unity features on or off through the
Package Manager. Enabling or disabling a package reduces the run-time build
size. For example, most projects don’t use the legacy **Particle System** A
component that simulates fluid entities such as liquids, clouds and flames by
generating and animating large numbers of small 2D images in the scene. [More
info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particlesystem). By removing the abstracted
package of this feature, the related code and resources are not part of the
final built product. Typically, these packages contain only the **package
manifest** Each package has a _manifest_ , which provides information about
the package to the Package Manager. The manifest contains information such as
the name of the package, its version, a description for users, dependencies on
other packages (if any), and other details. [More info](upm-manifestPkg.html)  
See in [Glossary](Glossary.html#Packagemanifest) and are bundled with Unity
(rather than available on the package registry).

#### Bundled package:

Unity stores _bundled_ packages in the [global cache](upm-cache.html) when you
install Unity. You can install these packages in your project even if you are
completely offline (not currently connected to the internet or a local
network).

#### Default package:

Unity automatically pre-installs a select number of _default_ packages (for
example, the Analytics Library, Unity Timeline, etc.) when you create a new
project. This differs from a **bundled package** Unity stores _bundled_
packages in the [global cache](upm-cache.html) when you install Unity. You can
install these packages in your project even if you are completely offline (not
currently connected to the internet or a local network).  
See in [Glossary](Glossary.html#Bundledpackage) because you don’t need to
install it and it differs from a **built-in package** _Built-in_ packages
allow users to toggle Unity features on or off through the Package Manager.
Enabling or disabling a package reduces the run-time build size. For example,
most projects don’t use the legacy Particle System. By removing the abstracted
package of this feature, the related code and resources are not part of the
final built product. Typically, these packages contain only the package
manifest and are bundled with Unity (rather than available on the package
registry).  
See in [Glossary](Glossary.html#Built-inpackage) because it extends Unity’s
features rather than being able to enable or disable them.

#### Direct dependency:

A **direct** dependency occurs when your project “requests” a specific package
version. To create a **direct dependency** A **direct** dependency occurs when
your project “requests” a specific package version. To create a direct
dependency, you add that package and version to the **dependencies** property
in your project manifest (expressed in the form
`package_name@package_version`). [More info](upm-dependencies.html)  
See in [Glossary](Glossary.html#Directdependency), you add that package and
version to the **dependencies** property in your **project manifest** Each
Unity project has a _project manifest_ , which acts as an entry point for the
Package Manager. This file must be available in the `<project>/Packages`
directory. The Package Manager uses it to configure many things, including a
list of dependencies for that project, as well as any package repository to
query for packages. [More info](upm-manifestPrj.html)  
See in [Glossary](Glossary.html#Projectmanifest) (expressed in the form
`package_name@package_version`). [More info](upm-dependencies.html)

#### Embedded package:

An _embedded_ package is a **mutable** You can change the contents of a
mutable package. This is the opposite of **immutable**. Only **Local
package****s** and **Embedded package****s** are mutable.  
See in [Glossary](Glossary.html#Mutable) package that you store under the
`Packages` directory at the root of a Unity project. This differs from most
packages which you download from a package server and are **immutable** You
cannot change the contents of an immutable (read-only) package. This is the
opposite of **mutable**. Most packages are immutable, including packages
downloaded from the package registry or by Git URL.  
See in [Glossary](Glossary.html#Immutable). [More info](upm-
concepts.html#Embedded)

#### Feature set:

A feature set is a collection of related packages that you can use to achieve
specific results in the Unity Editor. You can manage feature sets directly in
Unity’s Package Manager. [More info](FeatureSets.html)

#### Git dependency:

The Package Manager retrieves **Git dependencies** The Package Manager
retrieves Git dependencies from a Git repository directly rather than from a
package registry. Git dependencies use a Git URL reference instead of a
version, and there’s no guarantee about the package quality, stability,
validity, or even whether the version stated in its `package.json` file
respects Semantic Versioning rules with regards to officially published
releases of this package. [More info](upm-concepts.html#Git)  
See in [Glossary](Glossary.html#Gitdependency) from a Git repository directly
rather than from a package registry. **Git dependencies** use a Git URL
reference instead of a version, and there’s no guarantee about the package
quality, stability, validity, or even whether the version stated in its
`package.json` file respects Semantic Versioning rules with regards to
officially published releases of this package. [More info](upm-
concepts.html#Git)

#### Immutable:

You cannot change the contents of an **immutable** You cannot change the
contents of an immutable (read-only) package. This is the opposite of
**mutable**. Most packages are immutable, including packages downloaded from
the package registry or by Git URL.  
See in [Glossary](Glossary.html#Immutable) (read-only) package. This is the
opposite of **mutable** You can change the contents of a mutable package. This
is the opposite of **immutable**. Only **Local package****s** and **Embedded
package****s** are mutable.  
See in [Glossary](Glossary.html#Mutable). Most packages are **immutable** ,
including packages downloaded from the package registry or by Git URL.

#### Indirect dependency:

An **indirect** , or transitive dependency occurs when your project requests a
package which itself “depends on” another package. For example, if your
project depends on the `alembic@1.0.7` package which in turn depends on the
`timeline@1.0.0` package, then your project has an **direct dependency** A
**direct** dependency occurs when your project “requests” a specific package
version. To create a direct dependency, you add that package and version to
the **dependencies** property in your project manifest (expressed in the form
`package_name@package_version`). [More info](upm-dependencies.html)  
See in [Glossary](Glossary.html#Directdependency) on Alembic and an **indirect
dependency** An **indirect** , or transitive dependency occurs when your
project requests a package which itself “depends on” another package. For
example, if your project depends on the `alembic@1.0.7` package which in turn
depends on the `timeline@1.0.0` package, then your project has an direct
dependency on Alembic and an indirect dependency on Timeline. [More info](upm-
dependencies.html)  
See in [Glossary](Glossary.html#Indirectdependency) on Timeline. [More
info](upm-dependencies.html)

#### Local package:

A _local_ package already exists on the file system, usually outside the
project folder. To install the package, notify the Package Manager of its
location through the **Packages** window. [More info](upm-ui-local.html)

#### Manifest:

There are two types of manifest files: **project manifest** Each Unity project
has a _project manifest_ , which acts as an entry point for the Package
Manager. This file must be available in the `<project>/Packages` directory.
The Package Manager uses it to configure many things, including a list of
dependencies for that project, as well as any package repository to query for
packages. [More info](upm-manifestPrj.html)  
See in [Glossary](Glossary.html#Projectmanifest)**s** and **package manifest**
Each package has a _manifest_ , which provides information about the package
to the Package Manager. The manifest contains information such as the name of
the package, its version, a description for users, dependencies on other
packages (if any), and other details. [More info](upm-manifestPkg.html)  
See in [Glossary](Glossary.html#Packagemanifest)**s**.

#### Mutable:

You can change the contents of a **mutable** You can change the contents of a
mutable package. This is the opposite of **immutable**. Only **Local
package****s** and **Embedded package****s** are mutable.  
See in [Glossary](Glossary.html#Mutable) package. This is the opposite of
**immutable** You cannot change the contents of an immutable (read-only)
package. This is the opposite of **mutable**. Most packages are immutable,
including packages downloaded from the package registry or by Git URL.  
See in [Glossary](Glossary.html#Immutable). Only **Local package** A _local_
package already exists on the file system, usually outside the project folder.
To install the package, notify the Package Manager of its location through the
**Packages** window. [More info](upm-ui-local.html)  
See in [Glossary](Glossary.html#Localpackage)**s** and **Embedded package** An
_embedded_ package is a mutable package that you store under the `Packages`
directory at the root of a Unity project. This differs from most packages
which you download from a package server and are immutable. [More info](upm-
concepts.html#Embedded)  
See in [Glossary](Glossary.html#Embeddedpackage)**s** are **mutable**.

#### Package manifest:

Each package has a _manifest_ , which provides information about the package
to the Package Manager. The manifest contains information such as the name of
the package, its version, a description for users, dependencies on other
packages (if any), and other details. [More info](upm-manifestPkg.html)

#### Preview package:

A _preview_ package is in development and not yet ready for production. A
package in preview might be at any stage of development, from the initial
stages to near completion.

#### Project manifest:

Each Unity project has a _project manifest_ , which acts as an entry point for
the Package Manager. This file must be available in the `<project>/Packages`
directory. The Package Manager uses it to configure many things, including a
list of dependencies for that project, as well as any package repository to
query for packages. [More info](upm-manifestPrj.html)

#### Verified package:

When a package passes release cycle testing for a specific version of Unity,
it receives the _Verified For_ designation. This means that these packages are
guaranteed to work with the designated version of Unity.

## Performance terms

#### Profiler category:

Identifies the workload data for a Unity subsystem (for example, Rendering,
Scripting and Animation categories). Unity applies color-coding to categories
to visually distinguish between the types of data in the ****Profiler** A
window that helps you to optimize your game. It shows how much time is spent
in the various areas of your game. For example, it can report the percentage
of time spent rendering, animating, or in your game logic. [More
info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler)** window.

#### Profiler marker:

Placed in code to describe a CPU or GPU event that is then displayed in the
Unity **Profiler** A window that helps you to optimize your game. It shows how
much time is spent in the various areas of your game. For example, it can
report the percentage of time spent rendering, animating, or in your game
logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) window. Added to Unity code by
default, or you can use [ProfilerMarker
API](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilermarker-
guide.html) to add your own custom markers. [More info](profiler-markers.html)

#### Profiler counter:

Placed in code with the ProfilerCounter API to track metrics, such as the
number of enemies spawned in your game. [More
info](https://docs.unity3d.com/Packages/com.unity.profiling.core@latest/index.html?subfolder=/manual/profilercounter-
guide.html)

#### Profiler sample:

A set of data associated with a **Profiler** A window that helps you to
optimize your game. It shows how much time is spent in the various areas of
your game. For example, it can report the percentage of time spent rendering,
animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) marker, that the **Profiler** has
recorded and collected.

#### Profiler:

A window that helps you to optimize your game. It shows how much time is spent
in the various areas of your game. For example, it can report the percentage
of time spent rendering, animating, or in your game logic. [More
info](Profiler.html)

#### VSync:

Vertical synchronization (VSync) is a display setting that caps a game’s frame
rate to match the refresh rate of a monitor, to prevent image tearing.

#### VBlank:

Vertical blanking interval (VBlank) is the time between the end of the final
visible line of a frame and the beginning of the first visible line of the
next frame. This is the refresh interval as defined by a screen’s refresh
rate.

#### call stack:

A list of methods that were called at run time, organized as a last-in-first-
out stack.

#### overhead:

The amount of supporting code that the **Profiler** A window that helps you to
optimize your game. It shows how much time is spent in the various areas of
your game. For example, it can report the percentage of time spent rendering,
animating, or in your game logic. [More info](Profiler.html)  
See in [Glossary](Glossary.html#Profiler) needs to run. This overhead might
affect the performance of your application.

## Physics terms

#### Bounding volume:

A closed shape representing the edges and faces of a **collider** An invisible
shape that is used to handle physical collisions for an object. A collider
doesn’t need to be exactly the same shape as the object’s mesh - a rough
approximation is often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) or trigger.

#### box collider:

A cube-shaped **collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) component that handles
**collisions** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) for **GameObjects** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) like dice and ice cubes. [More
info](class-BoxCollider.html)

#### broad-phase collision detection:

A **collision** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection phase that computes pairs
of potentially overlapping objects by judging only their respective **bounding
volumes** A closed shape representing the edges and faces of a collider or
trigger.  
See in [Glossary](Glossary.html#Boundingvolume). [More
info](http://planning.cs.uiuc.edu/node214.html)

#### capsule collider:

A capsule-shaped **collider** An invisible shape that is used to handle
physical collisions for an object. A collider doesn’t need to be exactly the
same shape as the object’s mesh - a rough approximation is often more
efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) component that handles
**collisions** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) for **GameObjects** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) like barrels and character limbs.
[More info](class-CapsuleCollider.html)

#### Center of Mass:

Represents the average position of all mass in a **Rigidbody** A component
that allows a GameObject to be affected by simulated gravity and other forces.
[More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) for the purposes of physics
calculations. By default it is computed from all **colliders** An invisible
shape that is used to handle physical collisions for an object. A collider
doesn’t need to be exactly the same shape as the object’s mesh - a rough
approximation is often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) belonging to the **Rigidbody** , but
can be modified via script. [More info](../ScriptReference/Rigidbody-
centerOfMass.html)

#### Character Controller:

A simple, capsule-shaped **collider** An invisible shape that is used to
handle physical collisions for an object. A collider doesn’t need to be
exactly the same shape as the object’s mesh - a rough approximation is often
more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) component with specialized features
for behaving as a character in a game. Unlike true **collider** components, a
**Rigidbody** A component that allows a GameObject to be affected by simulated
gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) is not needed and the momentum
effects are not realistic. [More info](class-CharacterController.html)

#### Character Joint:

An extended ball-socket **joint** A physics component allowing a dynamic
connection between Rigidbody components, usually allowing some degree of
movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) which allows a **joint** to be limited
on each axis. Mainly used for Ragdoll effects. [More info](class-
CharacterJoint.html)

#### Cloth:

A component that works with the Skinned **Mesh** The main graphics primitive
of Unity. Meshes make up a large part of your 3D worlds. Unity supports
triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces
must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) Renderer to provide a physics-based
solution for simulating fabrics. [More info](class-Cloth.html)

#### Collider:

An invisible shape that is used to handle physical **collisions** A collision
occurs when the physics engine detects that the colliders of two GameObjects
make contact or overlap, when at least one has a Rigidbody component and is in
motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) for an object. A **collider** An
invisible shape that is used to handle physical collisions for an object. A
collider doesn’t need to be exactly the same shape as the object’s mesh - a
rough approximation is often more efficient and indistinguishable in gameplay.
[More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) doesn’t need to be exactly the same
shape as the object’s **mesh** The main graphics primitive of Unity. Meshes
make up a large part of your 3D worlds. Unity supports triangulated or
Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted
to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) \- a rough approximation is often more
efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)

#### Collision:

A **collision** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) occurs when the **physics engine**
A system that simulates aspects of physical systems so that objects can
accelerate correctly and be affected by collisions, gravity and other forces.
[More info](PhysicsSection.html)  
See in [Glossary](Glossary.html#PhysicsEngine) detects that the **colliders**
An invisible shape that is used to handle physical collisions for an object. A
collider doesn’t need to be exactly the same shape as the object’s mesh - a
rough approximation is often more efficient and indistinguishable in gameplay.
[More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) of two **GameObjects** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) make contact or overlap, when at
least one has a **Rigidbody** A component that allows a GameObject to be
affected by simulated gravity and other forces. [More info](class-
Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) component and is in motion. [More
info](CollidersOverview.html)

#### Collision Detection:

An automatic process performed by Unity which determines whether a moving
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) with a **Rigidbody** A component
that allows a GameObject to be affected by simulated gravity and other forces.
[More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) and **collider** An invisible shape
that is used to handle physical collisions for an object. A collider doesn’t
need to be exactly the same shape as the object’s mesh - a rough approximation
is often more efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) component has come into contact with
any other **colliders** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider). [More info](CollidersOverview.html)

#### Configurable Joint:

An extremely customizable **joint** A physics component allowing a dynamic
connection between Rigidbody components, usually allowing some degree of
movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) that other **joint** types are derived
from. It can be used to create anything from adapted versions of existing
**joints** A physics component allowing a dynamic connection between Rigidbody
components, usually allowing some degree of movement such as a hinge. [More
info](Joints.html)  
See in [Glossary](Glossary.html#joint) to custom designed and highly
specialized **joints**. [More info](class-ConfigurableJoint.html)

#### Constant Force:

A simple component for adding a **constant force** A simple component for
adding a constant force or torque to game objects with a Rigidbody. [More
info](class-ConstantForce.html)  
See in [Glossary](Glossary.html#ConstantForce) or torque to game objects with
a **Rigidbody** A component that allows a GameObject to be affected by
simulated gravity and other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody). [More info](class-
ConstantForce.html)

#### Constraints:

Settings on **Joint** A physics component allowing a dynamic connection
between Rigidbody components, usually allowing some degree of movement such as
a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) components which limit movement or
rotation. The type and number of constraints vary depending on the type of
**Joint**. [More info](2d-physics/joints/2d-joints-landing.html)

#### Contact Distance:

A **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) limit property that sets the minimum
distance tolerance between the **joint** position and the limit at which the
limit will be enforced. [More info](class-CharacterJoint.html)

#### continuous collision detection:

A **collision** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection method that calculates
and resolves **collisions** A collision occurs when the physics engine detects
that the colliders of two GameObjects make contact or overlap, when at least
one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) over the entire physics simulation
step. This can prevent fast-moving objects from tunnelling through walls
during a simulation step. [More info](ContinuousCollisionDetection.html)

#### Damping Ratio:

A **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) setting to control spring oscillation.
A higher **damping ratio** A joint setting to control spring oscillation. A
higher damping ratio means the spring will come to rest faster. [More
info](2d-physics/joints/fixed-joint-2d-reference.html)  
See in [Glossary](Glossary.html#DampingRatio) means the spring will come to
rest faster. [More info](2d-physics/joints/fixed-joint-2d-reference.html)

#### discrete collision detection:

A **collision** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection method that calculates
and resolves **collisions** A collision occurs when the physics engine detects
that the colliders of two GameObjects make contact or overlap, when at least
one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) based on the pose of objects at the
end of each physics simulation step. [More info](class-Rigidbody.html)

#### Dynamic Friction:

A **Physics Material** A physics asset for adjusting the friction and bouncing
effects of colliding objects. [More info](class-PhysicsMaterial.html)  
See in [Glossary](Glossary.html#PhysicsMaterial) property that defines the
friction for a **Rigidbody** A component that allows a GameObject to be
affected by simulated gravity and other forces. [More info](class-
Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) when it’s in motion. Lower values
mean less friction, so a setting of zero represents slipping on ice. [More
info](class-PhysicsMaterial.html)

#### Fixed Joint:

A **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) type that is completely constrained,
allowing two objects to be held together. Implemented as a spring so some
motion may still occur. [More info](class-FixedJoint.html)

#### Fixed Timestep:

A customizable frame-rate-independent interval that dictates when physics
calculations and FixedUpdate() events are performed. [More info](class-
TimeManager.html)

#### High Twist Limit:

The higher limit of a Character **Joint** A physics component allowing a
dynamic connection between Rigidbody components, usually allowing some degree
of movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint). [More info](class-CharacterJoint.html)

#### Hinge Joint:

A **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) that groups together two **Rigidbody**
A component that allows a GameObject to be affected by simulated gravity and
other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) components, constraining them to
move like they are connected by a hinge. It is perfect for doors, but can also
be used to model chains, pendulums and so on. [More info](class-
HingeJoint.html)

#### joint:

A physics component allowing a dynamic connection between **Rigidbody** A
component that allows a GameObject to be affected by simulated gravity and
other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) components, usually allowing some
degree of movement such as a hinge. [More info](Joints.html)

#### Low Twist Limit:

A **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) property that sets the lower limit of a
**joint**. [More info](class-CharacterJoint.html)

#### Mesh Collider:

A free-form **collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) component which accepts a **mesh**
The main graphics primitive of Unity. Meshes make up a large part of your 3D
worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs,
Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) reference to define its **collision** A
collision occurs when the physics engine detects that the colliders of two
GameObjects make contact or overlap, when at least one has a Rigidbody
component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) surface shape. [More info](class-
MeshCollider.html)

#### narrow-phase collision detection:

A **collision** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection phase that determines
whether the pairs of objects found in the broad phase will actually collide.
It then computes the contact points for those pairs and gives them to the
solver to use when solving **collisions** A collision occurs when the physics
engine detects that the colliders of two GameObjects make contact or overlap,
when at least one has a Rigidbody component and is in motion. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision). [More
info](http://planning.cs.uiuc.edu/node214.html)

#### Physics Material:

A physics asset for adjusting the friction and bouncing effects of colliding
objects. [More info](class-PhysicsMaterial.html)

#### Physics Engine:

A system that simulates aspects of physical systems so that objects can
accelerate correctly and be affected by **collisions** A collision occurs when
the physics engine detects that the colliders of two GameObjects make contact
or overlap, when at least one has a Rigidbody component and is in motion.
[More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision), gravity and other forces. [More
info](PhysicsSection.html)

#### Rig:

A skeletal hierarchy of **joints** A physics component allowing a dynamic
connection between Rigidbody components, usually allowing some degree of
movement such as a hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) for a **mesh** The main graphics
primitive of Unity. Meshes make up a large part of your 3D worlds. Unity
supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv
surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh). [More info](FBXImporter-Rig.html)

#### Rigidbody:

A component that allows a **GameObject** The fundamental object in Unity
scenes, which can represent characters, props, scenery, cameras, waypoints,
and more. A GameObject’s functionality is defined by the Components attached
to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to be affected by simulated
gravity and other forces. [More info](class-Rigidbody.html)

#### Self Collision:

A cloth property that prevents cloth from penetrating itself. [More
info](class-Cloth.html)

#### Soft Particles:

Particles that create semi-transparent effects like smoke, fog or fire. **Soft
particles** Particles that create semi-transparent effects like smoke, fog or
fire. Soft particles fade out as they approach an opaque object, to prevent
intersections with the geometry. [More info](shader-
StandardParticleShaders.html)  
See in [Glossary](Glossary.html#SoftParticles) fade out as they approach an
opaque object, to prevent intersections with the geometry. [More info](shader-
StandardParticleShaders.html)

#### speculative continuous collision detection:

A **collision** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection method that inflates
broad-phase AABB of moving objects according to their velocities. This enables
support for effects like rotations. [More
info](ContinuousCollisionDetection.html)

#### Sphere Collider:

A sphere-shaped **collider** An invisible shape that is used to handle
physical collisions for an object. A collider doesn’t need to be exactly the
same shape as the object’s mesh - a rough approximation is often more
efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) component that handles
**collisions** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) for **GameObjects** The fundamental
object in Unity scenes, which can represent characters, props, scenery,
cameras, waypoints, and more. A GameObject’s functionality is defined by the
Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) like balls or other things that
can be roughly approximated as a sphere for the purposes of physics. [More
info](class-SphereCollider.html)

#### Spring Joint:

A **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) type that connects two **Rigidbody** A
component that allows a GameObject to be affected by simulated gravity and
other forces. [More info](class-Rigidbody.html)  
See in [Glossary](Glossary.html#Rigidbody) components together but allows the
distance between them to change as though they were connected by a spring.
[More info](class-SpringJoint.html)

#### Swing Axis:

A **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) property that defines the axis around
which the **joint** can swing. [More info](class-CharacterJoint.html)

#### Swing Limit:

A **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) property that limits the rotation
around one element of the defined **Swing Axis** A joint property that defines
the axis around which the joint can swing. [More info](class-
CharacterJoint.html)  
See in [Glossary](Glossary.html#SwingAxis). [More info](class-
CharacterJoint.html)

#### Target Position:

A **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) property to set the **target position**
A joint property to set the target position that the joint’s drive force
should move it to. [More info](class-ConfigurableJoint.html)  
See in [Glossary](Glossary.html#TargetPosition) that the **joint** ’s drive
force should move it to. [More info](class-ConfigurableJoint.html)

#### Target Velocity:

A **joint** A physics component allowing a dynamic connection between
Rigidbody components, usually allowing some degree of movement such as a
hinge. [More info](Joints.html)  
See in [Glossary](Glossary.html#joint) property to set the desired velocity
with which the **joint** should move to the **Target Position** A joint
property to set the target position that the joint’s drive force should move
it to. [More info](class-ConfigurableJoint.html)  
See in [Glossary](Glossary.html#TargetPosition) under the drive force. [More
info](class-ConfigurableJoint.html)

#### Terrain Collider:

A terrain-shaped **collider** An invisible shape that is used to handle
physical collisions for an object. A collider doesn’t need to be exactly the
same shape as the object’s mesh - a rough approximation is often more
efficient and indistinguishable in gameplay. [More
info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) component that handles
**collisions** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) for **collision** A collision
occurs when the physics engine detects that the colliders of two GameObjects
make contact or overlap, when at least one has a Rigidbody component and is in
motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) surface with the same shape as the
**Terrain** The landscape in your scene. A Terrain GameObject adds a large
flat plane to your scene and you can use the Terrain’s Inspector window to
create a detailed landscape. [More info](terrain-UsingTerrains.html)  
See in [Glossary](Glossary.html#Terrain) object it is attached to. [More
info](class-TerrainCollider.html)

#### Wheel Collider:

A special **collider** An invisible shape that is used to handle physical
collisions for an object. A collider doesn’t need to be exactly the same shape
as the object’s mesh - a rough approximation is often more efficient and
indistinguishable in gameplay. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collider) for grounded vehicles. It has built-
in **collision** A collision occurs when the physics engine detects that the
colliders of two GameObjects make contact or overlap, when at least one has a
Rigidbody component and is in motion. [More info](CollidersOverview.html)  
See in [Glossary](Glossary.html#Collision) detection, wheel physics, and a
slip-based tire friction model. It can be used for objects other than wheels,
but it is specifically designed for vehicles with wheels. [More info](class-
WheelCollider.html)

## Platforms terms

#### ADB:

An Android Debug Bridge (ADB). You can use an **ADB** An Android Debug Bridge
(ADB). You can use an ADB to deploy an Android package (APK) manually after
building. [More info](https://developer.android.com/studio/command-
line/adb.html)  
See in [Glossary](Glossary.html#ADB) to deploy an Android package (APK)
manually after building. [More
info](https://developer.android.com/studio/command-line/adb.html)

#### AOT Compilation:

Ahead of Time (AOT) compilation is an optimization method used by all
platforms except iOS for optimizing the size of the built player. . [More
info](iphone-playerSizeOptimization.html)

#### APK:

The Android Package format output by Unity. An APK is automatically deployed
to your device when you select File > Build & Run. [More info](android-
BuildProcess.html)

#### Cache API:

A Javascript API to store network request and response pairs in the browser
cache. [More info](https://developer.mozilla.org/en-US/docs/Web/API/Cache)

#### AR:

Augmented Reality [More info](AROverview.html)

#### Augmented Reality:

Augmented Reality (AR) uses computer graphics or video composited on top of a
live video feed to augment the view and create interaction with real and
virtual objects. [More info](AROverview.html)

#### Closed platform:

Includes platforms that require confidentiality and legal agreements with the
platform provider for using their developer tools and hardware. These
platforms aren’t open to development unless you have an established
relationship with the provider. For example PlayStation®, Game Core for Xbox®,
and Nintendo®.

#### Emscripten:

The toolchain that Unity uses to convert from C and C++ to WebAssembly. [More
info](https://emscripten.org)

#### Gradle:

An Android build system that automates several build processes. This
automation means that many common build errors are less likely to occur. [More
info](android-gradle-overview.html)

#### Android Keystore:

An Android system that lets you store cryptographic key entries for enhanced
device security. [More info](class-PlayerSettingsAndroid.html#projectkeystore)

#### Mixed Reality:

Mixed Reality (MR) combines its own virtual environment with the user’s real-
world environment and allows them to interact with each other.

#### MR:

Mixed Reality

#### ODR:

On-demand resources (ODR) is a feature available for the iOS and tvOS
platforms, from version 9.0 of iOS and tvOS onwards. It allows you to reduce
the size of your application by separating the core assets (those that are
needed from application startup) from assets which may be optional, or which
appear in later levels of your game. [More info](AppThinning.html)

#### PhotoCapture:

An API that enables you to take photos from a HoloLens web **camera** A
component which creates an image of a particular viewpoint in your scene. The
output is either drawn to the screen or captured as a texture. [More
info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) and store them in memory or on disk.
[More info](../ScriptReference/Windows.WebCam.PhotoCapture.html)

#### Progressive Web App:

A software application that’s delivered through the web. It uses certain
browser features to create a user experience on par with a native application.
[More info](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)

#### Unity Remote:

A downloadable app designed to help with Android, iOS and tvOS development.
The app connects with Unity while you are running your project in Play Mode
from the Unity Editor. [More info](UnityRemote5.html)

#### Virtual Reality:

Virtual Reality (VR) immerses users in an artificial 3D world of realistic
images and sounds, using a headset and motion tracking. [More
info](VROverview.html)

#### VR:

Virtual Reality [More info](VROverview.html)

#### XR:

An umbrella term encompassing **Virtual Reality** Virtual Reality (VR)
immerses users in an artificial 3D world of realistic images and sounds, using
a headset and motion tracking. [More info](VROverview.html)  
See in [Glossary](Glossary.html#VirtualReality) (VR), **Augmented Reality**
Augmented Reality (AR) uses computer graphics or video composited on top of a
live video feed to augment the view and create interaction with real and
virtual objects. [More info](AROverview.html)  
See in [Glossary](Glossary.html#AugmentedReality) (AR) and **Mixed Reality**
Mixed Reality (MR) combines its own virtual environment with the user’s real-
world environment and allows them to interact with each other.  
See in [Glossary](Glossary.html#MixedReality) (MR) applications. Devices
supporting these forms of interactive applications can be referred to as
**XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality
(AR) and Mixed Reality (MR) applications. Devices supporting these forms of
interactive applications can be referred to as XR devices. [More
info](XR.html)  
See in [Glossary](Glossary.html#XR) devices. [More info](XR.html)

## Scripting terms

#### Cache API:

A Javascript API to store network request and response pairs in the browser
cache. [More info](https://developer.mozilla.org/en-US/docs/Web/API/Cache)

#### Event System:

A way of sending events to objects in the application based on input, be it
keyboard, mouse, touch, or custom input. The **Event System** A way of sending
events to objects in the application based on input, be it keyboard, mouse,
touch, or custom input. The Event System consists of a few components that
work together to send events. [More info](UIE-Runtime-Event-System.html)  
See in [Glossary](Glossary.html#EventSystem) consists of a few components that
work together to send events. [More info](UIE-Runtime-Event-System.html)

#### IL2CPP:

A Unity-developed scripting back-end which you can use as an alternative to
Mono when building projects for some platforms. [More info](./scripting-
backends-il2cpp.html)

#### mcs:

The Mono C# compiler file format. [More info](platform-dependent-
compilation.html)

#### Mono:

A **scripting backend** A framework that powers scripting in Unity. Unity
supports three different scripting backends depending on target platform:
Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two:
.NET and IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend) used in Unity. [More
info](./scripting-backends-il2cpp.html)

#### MonoDevelop:

An integrated development environment (IDE) supplied with Unity 2017.3 and
previous versions. From Unity 2018.1 onwards, **MonoDevelop** An integrated
development environment (IDE) supplied with Unity 2017.3 and previous
versions. From Unity 2018.1 onwards, MonoDevelop is replaced by Visual Studio.
[More info](https://www.monodevelop.com/)  
See in [Glossary](Glossary.html#MonoDevelop) is replaced by Visual Studio.
[More info](https://www.monodevelop.com/)

#### Scripting Backend:

A framework that powers scripting in Unity. Unity supports three different
**scripting backends** A framework that powers scripting in Unity. Unity
supports three different scripting backends depending on target platform:
Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two:
.NET and IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend) depending on target
platform: Mono, .NET and **IL2CPP** A Unity-developed scripting back-end which
you can use as an alternative to Mono when building projects for some
platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP). Universal Windows Platform, however,
supports only two: .NET and **IL2CPP**. [More info](scripting-backends.html)

#### Scripting Event:

A way of allowing a user-driven callback to persist from edit time to run time
without the need for additional programming and script configuration [More
info](UIE-Runtime-Event-System.html)

#### Scripts:

A piece of code that allows you to create your own Components, trigger game
events, modify Component properties over time and respond to user input in any
way you like. [More info](creating-scripts.html)

#### Tag:

A reference word which you can assign to one or more **GameObjects** The
fundamental object in Unity scenes, which can represent characters, props,
scenery, cameras, waypoints, and more. A GameObject’s functionality is defined
by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) to help you identify
**GameObjects** for scripting purposes. For example, you might define and
“Edible” Tag for any item the player can eat in your game. [More
info](Tags.html)

#### Test Framework,Test Runner:

The Test Framework package (formerly called the Test Runner) is a Unity tool
that tests your code in both Edit mode and Play mode, and also on target
platforms such as Standalone, Android, or iOS. [More
info](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)

#### Texture Format:

A file format for handling textures during real-time rendering by 3D graphics
hardware, such as a graphics card or mobile device. [More info](class-
TextureImporterOverride)

## Services terms

#### Build Automation:

A continuous integration service for Unity projects that automates the process
of creating builds on Unity’s servers. [More
info](https://docs.unity.com/devops/en/manual/unity-build-automation)

#### Services:

A Unity facility that provides a growing range of complimentary services to
help you make games and engage, retain and monetize audiences. [More
info](UnityServices.html)

#### Unity Build Automation:

See **Build Automation** A continuous integration service for Unity projects
that automates the process of creating builds on Unity’s servers. [More
info](https://docs.unity.com/devops/en/manual/unity-build-automation)  
See in [Glossary](Glossary.html#BuildAutomation)

#### Unity Cloud Diagnostics:

A suite of cloud-enabled tools that help you collect and identify issues that
users encounter with your apps. [More
info](https://docs.unity.com/ugs/manual/cloud-
diagnostics/manual/CloudDiagnostics/WelcometoCloudDiagnostics)

## UI terms

#### Canvas:

The area that contains all **UI**(User Interface) Allows a user to interact
with your application. Unity currently supports three UI systems. [More
info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) elements in a **scene** A Scene contains
the environments and menus of your game. Think of each unique Scene file as a
unique level. In each Scene, you place your environments, obstacles, and
decorations, essentially designing and building your game in pieces. [More
info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene). The Canvas area is shown as a
rectangle in the **Scene** A Scene contains the environments and menus of your
game. Think of each unique Scene file as a unique level. In each Scene, you
place your environments, obstacles, and decorations, essentially designing and
building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) View. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/UICanvas.html)

#### Canvas Group:

A group of **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) elements within a Canvas. Use a **Canvas
Group** A group of UI elements within a Canvas. Use a Canvas Group to control
a group of UI elements collectively without needing to handle them each
individually. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/class-
CanvasGroup.html)  
See in [Glossary](Glossary.html#CanvasGroup) to control a group of **UI**
elements collectively without needing to handle them each individually. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/class-
CanvasGroup.html)

#### Canvas Renderer:

Renders a graphical **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) object contained within a Canvas. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/class-
CanvasRenderer.html)

#### Canvas Scaler:

Controls the overall scale and **pixel** The smallest unit in a computer
image. Pixel size depends on your screen resolution. Pixel lighting is
calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) density of all **UI**(User Interface)
Allows a user to interact with your application. Unity currently supports
three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) elements in the Canvas, including font
sizes and image borders. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-
CanvasScaler.html)

#### Image control:

An Image control displays a non-interactive image to the user, such as a
decoration and icon. You can change the image from a script to reflect changes
in other controls. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-
Image.html)

#### Interactable:

A **UI**(User Interface) Allows a user to interact with your application.
Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) component property that determines whether
the component can accept input. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-
Selectable.html)

#### UI Mask:

A **visual component** A component that enables you to easily create GUI-
specific functionality. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/UIVisualComponents.html)  
See in [Glossary](Glossary.html#VisualComponent) that lets you restrict images
from view to only a small section of an image. For instance, you can apply a
Mask to a Panel **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) element to block all child images from
view. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-
Mask.html)

#### Raw image:

A Visual **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI) Component that displays a non-interactive
image to the user. This can be used for decoration, icons, and so on, and the
image can also be changed from a script to reflect changes in other controls.
[More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-
RawImage.html)

#### ScrollView:

A **UI**(User Interface) Allows a user to interact with your application.
Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) Control which displays a large set of
Controls in a viewable area that you can see by using a scrollbar. [More
info](UIE-uxml-element-ScrollView.html)

#### Shadow:

A **UI**(User Interface) Allows a user to interact with your application.
Unity currently supports three UI systems. [More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) component that adds a simple outline
effect to graphic components such as Text or Image. It must be on the same
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) as the graphic component. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-
Shadow.html)

#### Stencil masking meshes:

Overflow hidden with either rounded corners or vector image background.

#### Text:

A non-interactive piece of text to the user. This can be used to provide
captions or labels for other GUI controls or to display instructions or other
text. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-
Text.html)

#### TextField control:

A **TextField control** A TextField control displays a non-interactive piece
of text to the user, such as a caption, label for other GUI controls, or
instruction. [More info](gui-Controls.html)  
See in [Glossary](Glossary.html#TextFieldcontrol) displays a non-interactive
piece of text to the user, such as a caption, label for other GUI controls, or
instruction. [More info](gui-Controls.html)

#### Text Input Field:

A field that allows the user to input a Text string [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-
InputField.html)

#### Toggle:

A checkbox that allows the user to switch an option on or off. [More
info](UIE-uxml-element-Toggle.html)

#### Toolbar:

A row of buttons and basic controls at the top of the Unity Editor that allows
you to interact with the Editor in various ways (e.g. scaling, translation).
[More info](Toolbar.html)

#### UI:

(User Interface) Allows a user to interact with your application. Unity
currently supports three **UI**(User Interface) Allows a user to interact with
your application. Unity currently supports three UI systems. [More info](UI-
system-compare.html)  
See in [Glossary](Glossary.html#UI) systems. [More info](UI-system-
compare.html)

#### Visual Component:

A component that enables you to easily create GUI-specific functionality.
[More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/UIVisualComponents.html)

#### Visual tree:

An object graph, made of lightweight nodes, that holds all the elements in a
window or panel. It defines every **UI**(User Interface) Allows a user to
interact with your application. Unity currently supports three UI systems.
[More info](UI-system-compare.html)  
See in [Glossary](Glossary.html#UI) you build with the **UI** Toolkit.

#### Visual element:

A node of a **visual tree** An object graph, made of lightweight nodes, that
holds all the elements in a window or panel. It defines every UI you build
with the UI Toolkit.  
See in [Glossary](Glossary.html#Visualtree) that instantiates or derives from
the C# [`VisualElement`](../ScriptReference/UIElements.VisualElement.html)
class. You can style the look, define the behaviour, and display it on screen
as part of the **UI**(User Interface) Allows a user to interact with your
application. Unity currently supports three UI systems. [More info](UI-system-
compare.html)  
See in [Glossary](Glossary.html#UI). [More info](UIE-VisualTree.html)

[](udp-troubleshooting.html)

UDP troubleshooting

[](Glossary.html)

Glossary

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

