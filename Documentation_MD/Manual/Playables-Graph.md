[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Playables-Graph.html)
  * [中文](/cn/current/Manual/Playables-Graph.html)
  * [日本語](/ja/current/Manual/Playables-Graph.html)
  * [한국어](/kr/current/Manual/Playables-Graph.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Playables-Graph.html)
  * [中文](/cn/current/Manual/Playables-Graph.html)
  * [日本語](/ja/current/Manual/Playables-Graph.html)
  * [한국어](/kr/current/Manual/Playables-Graph.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Playables API](Playables.html)
  * The PlayableGraph

[](Playables.html)

Playables API

[](Playables-ScriptPlayable.html)

ScriptPlayable and PlayableBehaviour

# The PlayableGraph

The PlayableGraph defines a set of playable outputs that are bound to a
**GameObject** The fundamental object in Unity scenes, which can represent
characters, props, scenery, cameras, waypoints, and more. A GameObject’s
functionality is defined by the Components attached to it. [More info](class-
GameObject.html)  
See in [Glossary](Glossary.html#GameObject) or [component](Components.html)A
functional part of a GameObject. A GameObject can contain any number of
components. Unity has many built-in components, and you can create your own by
writing scripts that inherit from MonoBehaviour. [More
info](UsingComponents.html)  
See in [Glossary](Glossary.html#component). The PlayableGraph also defines a
set of **playables** An API that provides a way to create tools, effects or
other gameplay mechanisms by organizing and evaluating data sources in a tree-
like structure known as the PlayableGraph. [More info](Playables.html)  
See in [Glossary](Glossary.html#Playables) and their relationships. Figure 1
provides an example.

The PlayableGraph is responsible for the life cycle of its playables and their
outputs. Use the PlayableGraph to create, connect, and destroy playables.

![Figure 1: A sample PlayableGraph](../uploads/Main/PlayablesGraph0.png)
Figure 1: A sample PlayableGraph

In Figure 1, when displaying a PlayableGraph, the term “Playable” is removed
from the names of graph nodes to make it more compact. For example, the node
named “AnimationClipPlayable” is shown as “AnimationClip.”

![](../uploads/Main/PlayablesGraphWarning.png)

A playable is a C# struct that implements the IPlayable interface. It is used
to define its relationship with other playables. Likewise, a playable output
is a C# struct that implements IPlayableOutput and is used to define the
output of a PlayableGraph.

Figure 2 shows the most common core playable types. Figure 3 shows the core
playable output types.

![Figure 2: Core playable types](../uploads/Main/PlayablesGraph1.png) Figure
2: Core playable types ![Figure 3: Core playable output
types](../uploads/Main/PlayablesGraph2.png) Figure 3: Core playable output
types

The playable core types and playable output types are implemented as C#
structs to avoid allocating [memory for garbage collection](performance-
managed-memory.html).

‘Playable’ is the base type for all playables, meaning that you can always
implicitly cast a playable to it. The opposite is not true, and an exception
will be thrown if a ‘Playable’ is explicitly casted into an incompatible type.
It also defines all the basic methods that can be executed on a playable. To
access type-specific methods, you need to cast our playable to the appropriate
type.

The same thing is true for ‘PlayableOutput’, it is the base type for all
playable outputs and it defines the basic methods.

Note: `Playable` and `PlayableOutput` do not expose a lot of methods. Instead,
the ‘PlayableExtensions’ and ‘PlayableOutputExtensions’ static classes provide
extension methods.

All non-abstract playables have a public static method `Create()` that creates
a playable of the corresponding type. The ‘Create()’ method always takes a
PlayableGraph as its first parameter, and that graph owns the newly created
playable. Additional parameters may be required for some type of playables.
Non-abstract playable outputs also expose a `Create()` method.

A valid playable output should be linked to a playable. If a playable output
is not linked to a playable, the playable output does nothing. To link a
playable output to a playable, use the `PlayableOutput.SetSourcePlayable()`
method. The linked playable acts as the root of the playable tree, for that
specific playable output.

To connect two playables together, use the `PlayableGraph.Connect()` method.
Note that some playables cannot have inputs.

Use the `PlayableGraph.Create()` static method to create a PlayableGraph.

Play a PlayableGraph with the `PlayableGraph.Play()` method.

Stop a playing PlayableGraph with the`PlayableGraph.Stop()` method.

Evaluate the state of a PlayableGraph, at a specific time, with the
`PlayableGraph.Evaluate()` method.

Destroy a PlayableGraph manually with the `PlayableGraph.Destroy()` method.
This method automatically destroys all playables and playable outputs that
were created by the PlayableGraph. You must manually call this destroy method
to destroy a PlayableGraph, otherwise Unity issues an error message.

* * *

  * 2017–07–04 Page published 

  * New in Unity [2017.1](../Manual/30_search.html?q=newin20171) NewIn20171

[](Playables.html)

Playables API

[](Playables-ScriptPlayable.html)

ScriptPlayable and PlayableBehaviour

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

