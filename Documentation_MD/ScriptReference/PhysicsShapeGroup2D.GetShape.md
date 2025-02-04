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

#  [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).GetShape

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

public [PhysicsShape2D](PhysicsShape2D.html) GetShape(int shapeIndex);

### Parameters

shapeIndex | The index of the shape stored the [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html). The shape index is zero-based with the shape group having a quantity of shapes specified by [shapeCount](PhysicsShapeGroup2D-shapeCount.html).  
---|---  
  
### Returns

**PhysicsShape2D** Returns the shape stored at the specified `shapeIndex`.

### Description

Gets the [PhysicsShape2D](PhysicsShape2D.html) stored at the specified
`shapeIndex`.

**NOTE** : Because the [PhysicsShape2D](PhysicsShape2D.html) is a struct, this
is a copy of the shape therefore changing the shape afterwards will not change
the [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create a shape group.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Add a Circle to the shape group.
            var circleShapeIndex = shapeGroup.AddCircle
                (
                    center: new [Vector2](Vector2.html)(-2f, 3f),
                    radius: 1f
                );  
      
            // Add a Capsule to the shape group.
            var capsuleShapeIndex = shapeGroup.AddCapsule
                (
                    vertex0: [Vector2.down](Vector2-down.html),
                    vertex1: [Vector2.up](Vector2-up.html),
                    radius: 0.5f
                );  
      
            // Validate the contents.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Circle](PhysicsShapeType2D.Circle.html), shapeGroup.GetShape(circleShapeIndex).shapeType);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)([PhysicsShapeType2D.Capsule](PhysicsShapeType2D.Capsule.html), shapeGroup.GetShape(capsuleShapeIndex).shapeType);
        }
    }
    

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

