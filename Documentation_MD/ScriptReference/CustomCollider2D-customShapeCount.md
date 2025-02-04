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

#  [CustomCollider2D](CustomCollider2D.html).customShapeCount

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

public int customShapeCount;

### Description

The total number of custom [PhysicsShape2D](PhysicsShape2D.html) assigned to
the Collider. (Read Only)

All the shapes represented here contain a total vertex count of
[customVertexCount](CustomCollider2D-customVertexCount.html).  
  
**NOTE** : This property should not be confused with
[Collider2D.shapeCount](Collider2D-shapeCount.html) which is a count of active
shapes on the [Collider2D](Collider2D.html). The
[CustomCollider2D](CustomCollider2D.html) has this property too. If a
[Collider2D](Collider2D.html) is disabled, inactive or in
[error](Collider2D-errorState.html) then the
[Collider2D.shapeCount](Collider2D-shapeCount.html) will be zero whereas the
[customShapeCount](CustomCollider2D-customShapeCount.html) will always be a
count of assigned custom [PhysicsShape2D](PhysicsShape2D.html).

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Fetch the custom collider.
            var customCollider = GetComponent<[CustomCollider2D](CustomCollider2D.html)>();  
      
            // Create a shape group.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Add a Circle to the shape group.
            shapeGroup.AddCircle
                (
                    center: new [Vector2](Vector2.html)(-1f, 0f),
                    radius: 0.5f
                );  
      
            // Add a box to the shape group.
            shapeGroup.AddBox
                (
                    center: new [Vector2](Vector2.html)(1f, 0f),
                    size: new [Vector2](Vector2.html)(1f, 1f)
                );  
      
            // Assign our shapes.
            customCollider.SetCustomShapes(shapeGroup);  
      
            // Validate the custom shape count.
            [Assert.AreApproximatelyEqual](Assertions.Assert.AreApproximatelyEqual.html)(shapeGroup.shapeCount, customCollider.customShapeCount);
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

