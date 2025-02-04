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

#  [StaticBatchingUtility](StaticBatchingUtility.html).Combine

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

## Declaration

public static void Combine([GameObject](GameObject.html) staticBatchRoot);

### Parameters

staticBatchRoot | The GameObject that should become the root of the combined batch.  
---|---  
  
### Description

Combines all children GameObjects of the `staticBatchRoot` for static
batching.

Static batching is a [draw call batching](../Manual/DrawCallBatching.html)
method that combines meshes that don't move to reduce [draw
calls](../Manual/optimizing-draw-calls.html). For more information about
static batching, see [Static batching](../Manual/static-batching.html).  
  
This method copies the mesh data of the GameObjects into a single internal
mesh. Each original GameObject is still present in the Scene which means Unity
can still cull them individually.  
  
All child GameObjects under the `staticBatchRoot` must be eligible for static
batching. For information on the eligibility requirements for static batching,
see [Static batching at runtime](../Manual/static-batching#runtime.html).  
  
After you combine the GameObjects, you can't change the
[Transform](Transform.html) properties of the children. However, you can
change the Transform properties of the `staticBatchRoot`. Doing so transforms
the entire combined batch.  
  
Note: You don't need to use this method with GameObjects you marked as
Batching Static in the Editor. Unity prepares these GameObjects for static
batching when it builds the Player.  
  
See also: [Mesh.CombineMeshes](Mesh.CombineMeshes.html),
[Mesh.isReadable](Mesh-isReadable.html).

* * *

## Declaration

public static void Combine(GameObject[] gos, [GameObject](GameObject.html)
staticBatchRoot);

### Parameters

gos | The GameObjects to prepare for static batching.  
---|---  
staticBatchRoot | The GameObject that should become the root of the combined batch.  
  
### Description

Combines all GameObjects in `gos` for static batching and treats
`staticBatchRoot` as the root.

Static batching is a [draw call batching](../Manual/DrawCallBatching.html)
method that combines meshes that don't move to reduce [draw
calls](../Manual/optimizing-draw-calls.html). For more information about
static batching, see [Static batching](../Manual/static-batching.html).  
  
This method copies the mesh data of the GameObjects into a single internal
mesh. Each original GameObject is still present in the Scene which means Unity
can still cull them individually.  
  
All GameObjects in `gos` must be eligible for static batching. For information
on what a GameObject needs to be eligible for static batching, see [Static
batching at runtime](../Manual/static-batching#runtime.html).  
  
After you combine the GameObjects, you can't change the
[Transform](Transform.html) properties of the children. However, you can
change the Transform properties of the `staticBatchRoot`. Doing so transforms
the entire combined batch.  
  
Note: You don't need to use this API on GameObjects you marked as Batching
Static in the Editor. Unity prepares these GameObjects for static batching
when it builds the Player.  
  
  
  
See also: [Mesh.CombineMeshes](Mesh.CombineMeshes.html),
[Mesh.isReadable](Mesh-isReadable.html).

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

