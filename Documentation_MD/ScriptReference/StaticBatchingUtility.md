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

# StaticBatchingUtility

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

### Description

StaticBatchingUtility can prepare your objects to take advantage of Unity's
static batching.

This step is useful as a performance optimization allowing engine to reduce
number of draw-calls dramatically, but keep amount of rendered geometry
intact.  
  
By calling one of the Combine methods you will create an internal mesh which
will contain combined geometry, however each original GameObject will be
present in the Scene and will be culled individually. The fact that
GameObjects can be culled individually allows run-time to render the same
amount of geometry as it would without batching, unlike combining geometry in
the modeling tool. Combining geometry in the modeling tool prevents efficient
culling and results in much higher amount of geometry being rendered.  
  
Note that you do not need to call Combine methods on objects which were
already marked as "Static" in the Editor. They will be prepared for static
batching automatically during the Build Player step.  
  
**IMPORTANT:** only objects with the same material can be batched, thus it is
useful to share as many textures/material as you can.

### Static Methods

[Combine](StaticBatchingUtility.Combine.html)| Combines all children
GameObjects of the staticBatchRoot for static batching.  
---|---  
  
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

