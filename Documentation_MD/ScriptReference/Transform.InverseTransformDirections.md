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

#  [Transform](Transform.html).InverseTransformDirections

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

public void InverseTransformDirections(Span<Vector3> directions);

### Parameters

directions | The directions to be transformed, each is replaced by the transformed version.  
---|---  
  
### Description

Transforms multiple directions from world space to local space overwriting
each original position with the transformed version. The opposite of
[Transform.TransformDirections](Transform.TransformDirections.html).

This operation is not affected by scale or position of the transform. The
transformed vectors have the same lengths as the originals.  
  
If you need the inverse operation to transform from local space to world space
you can use
[Transform.TransformDirections](Transform.TransformDirections.html)  
  
You should use
[Transform.InverseTransformPoints](Transform.InverseTransformPoints.html) if
the vectors represent positions in space rather than directions.  
  
Additional
resources:[Transform.InverseTransformDirection](Transform.InverseTransformDirection.html),
[Transform.TransformDirections](Transform.TransformDirections.html),
[Transform.InverseTransformPoints](Transform.InverseTransformPoints.html),
[Transform.InverseTransformVectors](Transform.InverseTransformVectors.html).

* * *

## Declaration

public void InverseTransformDirections(ReadOnlySpan<Vector3> directions,
Span<Vector3> transformedDirections);

### Parameters

directions | The directions to be transformed, these vectors are not modified by the function unless the `transformedDirections` span overlaps.  
---|---  
transformedDirections | Receives the transformed directions, must be the same length as the `directions` span otherwise an exception will be thrown. If this span overlaps `directions` other than representing the exact same elements the behaviour is undefined.  
  
### Description

Transforms multiple directions from world space to local space writing the
transformed positions to a possibly different location. The opposite of
[Transform.TransformDirections](Transform.TransformDirections.html).

This operation is not affected by scale or position of the transform. The
transformed vectors have the same lengths as the originals.  
  
If you need the inverse operation to transform from local space to world space
you can use
[Transform.TransformDirections](Transform.TransformDirections.html)  
  
You should use
[Transform.InverseTransformPoints](Transform.InverseTransformPoints.html) if
the vectors represent positions in space rather than directions.  
  
Additional
resources:[Transform.InverseTransformDirection](Transform.InverseTransformDirection.html),
[Transform.TransformDirections](Transform.TransformDirections.html),
[Transform.InverseTransformPoints](Transform.InverseTransformPoints.html),
[Transform.InverseTransformVectors](Transform.InverseTransformVectors.html).

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

