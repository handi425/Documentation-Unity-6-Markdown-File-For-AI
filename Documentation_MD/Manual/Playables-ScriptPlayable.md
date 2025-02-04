[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/Playables-ScriptPlayable.html)
  * [中文](/cn/current/Manual/Playables-ScriptPlayable.html)
  * [日本語](/ja/current/Manual/Playables-ScriptPlayable.html)
  * [한국어](/kr/current/Manual/Playables-ScriptPlayable.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/Playables-ScriptPlayable.html)
  * [中文](/cn/current/Manual/Playables-ScriptPlayable.html)
  * [日本語](/ja/current/Manual/Playables-ScriptPlayable.html)
  * [한국어](/kr/current/Manual/Playables-ScriptPlayable.html)

  * [Animation](AnimationSection.html)
  * [Mecanim Animation system](AnimationOverview.html)
  * [Playables API](Playables.html)
  * ScriptPlayable and PlayableBehaviour

[](Playables-Graph.html)

The PlayableGraph

[](Playables-Examples.html)

Playables Examples

# ScriptPlayable and PlayableBehaviour

To create your own custom playable, it must be inherited from the
PlayableBehaviour base class. ` public class MyCustomPlayableBehaviour :
PlayableBehaviour { // Implementation of the custom playable behaviour //
Override PlayableBehaviour methods as needed } `

To use a PlayableBehaviour as a custom playable, it also must be encapsulated
within a ScriptPlayable<> object. If you don’t have an instance of your custom
playable, you can create a ScriptPlayable<> for your object by calling:

    
    
    ScriptPlayable<MyCustomPlayableBehaviour>.Create(playableGraph);
    

If you already have an instance of your custom playable, you can wrap it with
a ScriptPlayable<> by calling:

    
    
    MyCustomPlayableBehaviour myPlayable = new MyCustomPlayableBehaviour();
    ScriptPlayable<MyCustomPlayableBehaviour>.Create(playableGraph, myPlayable);
    

In this case, the instance is cloned before it is assigned to the
ScriptPlayable<>. As it is, this code does exactly the same as the previous
code; the difference is that `myPlayable` can be a public property that would
be configured in the inspector, and you can then set up your behaviour for
each instance of your script.

You can get the PlayableBehaviour object from the ScriptPlayable<> by using
the `ScriptPlayable<T> .GetBehaviour()` method.

* * *

  * New in Unity [2017.1](../Manual/30_search.html?q=newin20171) NewIn20171

[](Playables-Graph.html)

The PlayableGraph

[](Playables-Examples.html)

Playables Examples

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

