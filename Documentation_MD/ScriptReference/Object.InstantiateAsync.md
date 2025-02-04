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

#  [Object](Object.html).InstantiateAsync

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

[Switch to Manual](../Manual/class-Object.html "Go to Object Component in the
Manual")

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original,
[InstantiateParameters](InstantiateParameters.html) parameters,
CancellationToken cancellationToken);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original,
[Transform](Transform.html) parent);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original,
[Vector3](Vector3.html) position, [Quaternion](Quaternion.html) rotation);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original,
[Vector3](Vector3.html) position, [Quaternion](Quaternion.html) rotation,
[InstantiateParameters](InstantiateParameters.html) parameters,
CancellationToken cancellationToken);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original,
[Transform](Transform.html) parent, [Vector3](Vector3.html) position,
[Quaternion](Quaternion.html) rotation);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int
count);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int
count, [InstantiateParameters](InstantiateParameters.html) parameters,
CancellationToken cancellationToken);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int
count, [Transform](Transform.html) parent);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int
count, [Vector3](Vector3.html) position, [Quaternion](Quaternion.html)
rotation);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int
count, [Vector3](Vector3.html) position, [Quaternion](Quaternion.html)
rotation, [InstantiateParameters](InstantiateParameters.html) parameters,
CancellationToken cancellationToken);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int
count, ReadOnlySpan<Vector3> positions, ReadOnlySpan<Quaternion> rotations);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int
count, ReadOnlySpan<Vector3> positions, ReadOnlySpan<Quaternion> rotations,
[InstantiateParameters](InstantiateParameters.html) parameters,
CancellationToken cancellationToken);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int
count, [Transform](Transform.html) parent, [Vector3](Vector3.html) position,
[Quaternion](Quaternion.html) rotation);

## Declaration

public static AsyncInstantiateOperation<T> InstantiateAsync(T original, int
count, [Transform](Transform.html) parent, ReadOnlySpan<Vector3> positions,
ReadOnlySpan<Quaternion> rotations);

### Parameters

original | An existing object that you want to make a copy of.  
---|---  
count | The number of new copies to create.  
parent | The parent that will be assigned to the new object or objects.  
position | The position for the new object or objects.  
rotation | The rotation for the new object or objects.  
positions | The read only span of positions for the new object or objects. The length of the array can be less than `count`, in which case Unity uses position[i % count].  
rotations | The read only span of rotations for the new object or objects. The length of the array can be less than `count`, in which case Unity uses rotation[i % count].  
parameters | A struct containing all the parameters  
  
### Returns

**AsyncInstantiateOperation <T>** An asynchronous operation that contains the
resulting objects.

### Description

Captures a snapshot of the original object (that must be related to some
GameObject) and returns the AsyncInstantiateOperation.

The operation is mainly asynchronous, but the last stage involving integration
and awake calls is executed on the main thread. The operation can be
cancelled, or the integration stage can be delayed using allowSceneActivation.
It is possible to yield a return operation or call its WaitForCompletion()
method to finish the operation in a synchronized way.  
  
For extra control you can use the overrides that take an
[InstantiateParameters](InstantiateParameters.html) struct. This includes
extra options like deciding between using local or world space, or to specify
a target scene for the objects.

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

