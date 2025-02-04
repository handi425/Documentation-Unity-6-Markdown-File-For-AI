[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

#  [Physics2D](Physics2D.html).simulationLayers

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

public static [LayerMask](LayerMask.html) simulationLayers;

### Description

The [Rigidbody2D](Rigidbody2D.html) and [Collider2D](Collider2D.html) layers
to simulate.

By default, [All Layers](Physics2D.AllLayers.html) are simulated, however if
you specify layers in this property then only the
[Rigidbody2D](Rigidbody2D.html) on those layers will be simulated. Along with
this, only contacts for [Collider2D](Collider2D.html) on the specified
layer(s) will be handled. Finally, only [joints](Joint2D.html) or
[effectors](Effector2D.html) on the specified layer(s) will be handled.  
  
This property is only used when the Physics2D.SimulationMode is in one of the
automatic simulation modes i.e.
[SimulationMode2D.FixedUpdate](SimulationMode2D.FixedUpdate.html) or
[SimulationMode2D.Update](SimulationMode2D.Update.html). When using
[SimulationMode2D.Script](SimulationMode2D.Script.html) and calling
[Physics2D.Simulate](Physics2D.Simulate.html), the simulation layers are pass
as an argument.  
  
Additional resources:
[Physics2D.simulationMode](Physics2D-simulationMode.html) and
[Physics2D.Simulate](Physics2D.Simulate.html).

Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

