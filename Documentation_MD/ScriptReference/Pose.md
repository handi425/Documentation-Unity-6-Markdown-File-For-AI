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

# Pose

struct in UnityEngine

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

Representation of a Position, and a Rotation in 3D Space

This structure is used primarily in XR applications to describe the current
"pose" of a device in 3D space.

### Static Properties

[identity](Pose-identity.html)| Shorthand for pose which represents zero
position, and an identity rotation.  
---|---  
  
### Properties

[forward](Pose-forward.html)| Returns the forward vector of the pose.  
---|---  
[position](Pose-position.html)| The position component of the pose.  
[right](Pose-right.html)| Returns the right vector of the pose.  
[rotation](Pose-rotation.html)| The rotation component of the pose.  
[up](Pose-up.html)| Returns the up vector of the pose.  
  
### Constructors

[Pose](Pose-ctor.html)| Creates a new pose with the given vector, and
quaternion values.  
---|---  
  
### Public Methods

[GetTransformedBy](Pose.GetTransformedBy.html)| Transforms the current pose
into the local space of the provided pose.  
---|---  
  
### Operators

[operator !=](Pose-operator_ne.html)| Returns true if two poses are not equal.  
---|---  
[operator ==](Pose-operator_eq.html)| Returns true if two poses are equal.  
  
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

