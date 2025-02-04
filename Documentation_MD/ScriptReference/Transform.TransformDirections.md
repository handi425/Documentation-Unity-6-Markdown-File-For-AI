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

#  [Transform](Transform.html).TransformDirections

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

[Switch to Manual](../Manual/class-Transform.html "Go to Transform Component
in the Manual")

## Declaration

public void TransformDirections(Span<Vector3> directions);

### Parameters

directions | The directions to be transformed, each is replaced by the transformed version.  
---|---  
  
### Description

Transforms multiple directions from local space to world space overwriting
each original direction with the transformed version.

This operation is not affected by scale or position of the transform. The
transformed vectors have the same length as the original versions.  
  
If you need the inverse operation to transform from world space to local space
you can use
[Transform.InverseTransformDirections](Transform.InverseTransformDirections.html)  
  
You should use [Transform.TransformPoints](Transform.TransformPoints.html) for
the conversion if the vectors represent positions rather than directions.  
  
Additional resources:
[Transform.TransformDirection](Transform.TransformDirection.html),
[Transform.InverseTransformDirections](Transform.InverseTransformDirections.html),
[Transform.TransformPoints](Transform.TransformPoints.html),
[Transform.TransformVectors](Transform.TransformVectors.html).

* * *

## Declaration

public void TransformDirections(ReadOnlySpan<Vector3> directions,
Span<Vector3> transformedDirections);

### Parameters

directions | The directions to be transformed, these vectors are not modified by the function unless the `transformedDirections` span overlaps.  
---|---  
transformedDirections | Receives the transformed directions, must be the same length as `directions` otherwise an exception will be thrown. If this span overlaps `directions` other than representing the exact same elements the behaviour is undefined.  
  
### Description

Transforms multiple directions from local space to world space writing the
transformed directions to a possibly different location.

This operation is not affected by scale or position of the transform. The
transformed vectors have the same length as the original versions.  
  
If you need the inverse operation to transform from world space to local space
you can use
[Transform.InverseTransformDirections](Transform.InverseTransformDirections.html)  
  
You should use [Transform.TransformPoints](Transform.TransformPoints.html) for
the conversion if the vectors represent positions rather than directions.  
  
Additional resources:
[Transform.TransformDirection](Transform.TransformDirection.html),
[Transform.InverseTransformDirections](Transform.InverseTransformDirections.html),
[Transform.TransformPoints](Transform.TransformPoints.html),
[Transform.TransformVectors](Transform.TransformVectors.html).

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

