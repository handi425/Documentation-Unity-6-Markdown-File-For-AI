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

# OpaqueSortMode

enumeration

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

Opaque object sorting mode of a [Camera](Camera.html).

Opaque objects are sorted by various criteria (sorting layers, shader queues,
materials, distance, lightmaps etc.) to maximize both the CPU efficiency
(reduce number of state changes and improve draw call batching), and to
maximize GPU efficiency (many GPUs prefer rough front-to-back rendering order
for faster rejection of invisible surfaces).  
  
By default, opaque objects are grouped in rough front-to-back buckets, on the
GPUs where doing that is beneficial. There are GPUs where doing this distance
based sorting is not really helpful (most notably, PowerVR/Apple GPUs), and so
on these GPUs the distance based sorting is not done by default.  
  
The [Camera.opaqueSortMode](Camera-opaqueSortMode.html) property lets you
override this default behavior. For example, you might want to never do
distance-based sorting for opaque objects, if you know you need much more CPU
performance than GPU performance.  
  
Additional resources: [Camera.opaqueSortMode](Camera-opaqueSortMode.html).

### Properties

[Default](Rendering.OpaqueSortMode.Default.html)| Default opaque sorting mode.  
---|---  
[FrontToBack](Rendering.OpaqueSortMode.FrontToBack.html)| Do rough front-to-
back sorting of opaque objects.  
[NoDistanceSort](Rendering.OpaqueSortMode.NoDistanceSort.html)| Do not sort
opaque objects by distance.  
  
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

