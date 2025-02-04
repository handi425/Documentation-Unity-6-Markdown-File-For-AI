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

# BlendTree

class in UnityEditor.Animations

/

Inherits from:[Motion](Motion.html)

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

Blend trees are used to blend continuously animation between their children.
They can either be 1D or 2D.

### Properties

[blendParameter](Animations.BlendTree-blendParameter.html)| Parameter that is
used to compute the blending weight of the children in 1D blend trees or on
the X axis of a 2D blend tree.  
---|---  
[blendParameterY](Animations.BlendTree-blendParameterY.html)| Parameter that
is used to compute the blending weight of the children on the Y axis of a 2D
blend tree.  
[blendType](Animations.BlendTree-blendType.html)| The Blending type can be
either 1D or different types of 2D.  
[children](Animations.BlendTree-children.html)| A copy of the list of the
blend tree child motions.  
[maxThreshold](Animations.BlendTree-maxThreshold.html)| Sets the maximum
threshold that will be used by the ChildMotion. Only used when
useAutomaticThresholds is true.  
[minThreshold](Animations.BlendTree-minThreshold.html)| Sets the minimum
threshold that will be used by the ChildMotion. Only used when
useAutomaticThresholds is true.  
[useAutomaticThresholds](Animations.BlendTree-useAutomaticThresholds.html)|
When active, the children's thresholds are automatically spread between 0 and
1.  
  
### Public Methods

[AddChild](Animations.BlendTree.AddChild.html)| Utility function to add a
child motion to a blend trees.  
---|---  
[CreateBlendTreeChild](Animations.BlendTree.CreateBlendTreeChild.html)|
Utility function to add a child blend tree to a blend tree.  
[RemoveChild](Animations.BlendTree.RemoveChild.html)| Utility function to
remove the child of a blend tree.  
  
### Inherited Members

### Properties

[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
---|---  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
---|---  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
---|---  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

