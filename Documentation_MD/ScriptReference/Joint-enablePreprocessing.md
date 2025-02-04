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

#  [Joint](Joint.html).enablePreprocessing

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

public bool enablePreprocessing;

### Description

Toggle preprocessing for this joint.

This flag has a connection with rigidbodies that have some of their rotational
degrees of freedom frozed. The common example is a 2D game that uses 3D
rigidbodies with some of their translational and rotational degrees of freedom
frozen.  
  
Rigidbody rotations freezing is internally implemented by setting an infinite
inertia around those frozen axes so that the body does not rotate because it's
very resistant to.  
  
This approach has some nice properties: most significantly it lets such bodies
to correctly go to sleep as opposed to the approach where we would cancel out
the rotations around the frozen axes as a post-solver step.  
  
However the downside is that very stiff solver constraints can be generated
when such bodies are connected with joints. When the flag is set, PhysX would
ignore constraints that produce huge impulses generating only a small change
in velocity.  
  
Whilst it may reduce the overall accuracy of the joint simulation, it's been
proven to help with overconstrained configurations like in the 2D case.

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

