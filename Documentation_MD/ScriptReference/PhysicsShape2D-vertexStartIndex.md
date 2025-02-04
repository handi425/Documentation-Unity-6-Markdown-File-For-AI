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

#  [PhysicsShape2D](PhysicsShape2D.html).vertexStartIndex

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

public int vertexStartIndex;

### Description

The start index for the geometry of this shape within the
[PhysicsShapeGroup2D](PhysicsShapeGroup2D.html).

Multiple [PhysicsShape2D](PhysicsShape2D.html) in a
[PhysicsShapeGroup2D](PhysicsShapeGroup2D.html) are represented as a single
list of vertices. This index is the start of this shape within that list.  
  
Additional resources:
[GetShapeVertex](PhysicsShapeGroup2D.GetShapeVertex.html),
[GetShapeVertices](PhysicsShapeGroup2D.GetShapeVertices.html).

    
    
    using UnityEngine;
    using UnityEngine.Assertions;  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Create a shape group.
            var shapeGroup = new [PhysicsShapeGroup2D](PhysicsShapeGroup2D.html)();  
      
            // Add a Capsule to the shape group.
            var capsuleShapeIndex = shapeGroup.AddCapsule
                (
                    vertex0: [Vector2.down](Vector2-down.html),
                    vertex1: [Vector2.up](Vector2-up.html),
                    radius: 0.5f
                );  
      
            // Add a Circle to the shape group.
            var circleShapeIndex = shapeGroup.AddCircle
                (
                    center: new [Vector2](Vector2.html)(-2f, 3f),
                    radius: 1f
                );  
      
            // Fetch the shapes.
            var capsuleShape = shapeGroup.GetShape(capsuleShapeIndex);
            var circleShape = shapeGroup.GetShape(circleShapeIndex);  
      
            // Validate the shape vertex count.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(2, capsuleShape.vertexCount);
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(1, circleShape.vertexCount);  
      
            // Validate the Capsule vertex start index.
            // NOTE: The Capsule is the first shape so its index is 0.
            //  It has 2 vertices at indices 0 and 1.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(0, capsuleShape.vertexStartIndex);  
      
            // Validate the Circle vertex start index.
            // NOTE: The Circle is the second shape so its index is 0.
            // It comes after the Capsule which has 2 vertices at indices 0 and 1 so
            // the Circle start index is 2.
            [Assert.AreEqual](Assertions.Assert.AreEqual.html)(2, circleShape.vertexStartIndex);
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

