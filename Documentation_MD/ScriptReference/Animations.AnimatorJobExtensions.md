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

# AnimatorJobExtensions

class in UnityEngine.Animations

/

Implemented in:[UnityEngine.AnimationModule](UnityEngine.AnimationModule.html)

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

Static class providing extension methods for [Animator](Animator.html) and the
animation C# jobs.

The extension methods in this class can directly be used on an
[Animator](Animator.html).  
  
Additional resources:
[IAnimationJobPlayable](Animations.IAnimationJobPlayable.html).

### Static Methods

[AddJobDependency](Animations.AnimatorJobExtensions.AddJobDependency.html)|
Creates a dependency between animator jobs and the job represented by the
supplied job handle. To add multiple job dependencies, call this method for
each job that need to run before the Animator's jobs.  
---|---  
[BindCustomStreamProperty](Animations.AnimatorJobExtensions.BindCustomStreamProperty.html)|
Create a custom property in the AnimationStream to pass extra data to
downstream animation jobs in your graph. Custom properties created in the
AnimationStream do not exist in the scene.  
[BindSceneProperty](Animations.AnimatorJobExtensions.BindSceneProperty.html)|
Create a PropertySceneHandle representing the new binding on the Component
property of a Transform in the Scene.  
[BindSceneTransform](Animations.AnimatorJobExtensions.BindSceneTransform.html)|
Create a TransformSceneHandle representing the new binding between the
Animator and a Transform in the Scene.  
[BindStreamProperty](Animations.AnimatorJobExtensions.BindStreamProperty.html)|
Create a PropertyStreamHandle representing the new binding on the Component
property of a Transform already bound to the Animator.  
[BindStreamTransform](Animations.AnimatorJobExtensions.BindStreamTransform.html)|
Create a TransformStreamHandle representing the new binding between the
Animator and a Transform already bound to the Animator.  
[CloseAnimationStream](Animations.AnimatorJobExtensions.CloseAnimationStream.html)|
Close a stream that has been opened using OpenAnimationStream.  
[OpenAnimationStream](Animations.AnimatorJobExtensions.OpenAnimationStream.html)|
Open a new stream on the Animator.  
[ResolveAllSceneHandles](Animations.AnimatorJobExtensions.ResolveAllSceneHandles.html)|
Newly created handles are always resolved lazily on the next access when the
jobs are run. To avoid a cpu spike while evaluating the jobs you can manually
resolve all handles from the main thread.  
[ResolveAllStreamHandles](Animations.AnimatorJobExtensions.ResolveAllStreamHandles.html)|
Newly created handles are always resolved lazily on the next access when the
jobs are run. To avoid a cpu spike while evaluating the jobs you can manually
resolve all handles from the main thread.  
[UnbindAllSceneHandles](Animations.AnimatorJobExtensions.UnbindAllSceneHandles.html)|
Removes all PropertySceneHandles and TransformSceneHandles associated with the
Animator instance. Use this method to manage the lifecycle of scene handles
when the animated hierarchy changes.  
[UnbindAllStreamHandles](Animations.AnimatorJobExtensions.UnbindAllStreamHandles.html)|
Removes all PropertyStreamHandles and TransformStreamHandles associated with
the Animator instance. Use this method to manage the lifecycle of stream
handles when the animated hierarchy changes.  
  
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

