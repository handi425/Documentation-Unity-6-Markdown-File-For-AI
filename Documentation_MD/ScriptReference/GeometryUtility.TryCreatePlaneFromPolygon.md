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

#  [GeometryUtility](GeometryUtility.html).TryCreatePlaneFromPolygon

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

public static bool TryCreatePlaneFromPolygon(Vector3[] vertices, out
[Plane](Plane.html) plane);

### Parameters

vertices | An array of vertex positions that define the shape of a polygon.  
---|---  
plane | A valid plane that goes through the vertices.  
  
### Returns

**bool** Returns true on success, false if Unity did not create a plane from
the vertices.

### Description

[GeometryUtility.TryCreatePlaneFromPolygon](GeometryUtility.TryCreatePlaneFromPolygon.html)
creates a plane from the given list of `vertices` that define the polygon, as
long as they do not characterize a straight line or zero area.

There must be at least three vertices to create the plane; zero, one or two
vertices cause `false` to return with no plane. This works for concave
polygons and polygons with multiple aligned vertices, but not for self-
intersecting polygons.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    // [GeometryUtility.TryCreatePlaneFromPolygon](GeometryUtility.TryCreatePlaneFromPolygon.html) - example  
      
    // Attempt to draw a plane through selected positions.
    // Seven positions are generated close to the origin. Each position
    // will be in a random +/-1 xz area and random -0.5/0.5 y height.
    // Use these random positions for the array of vertices.
    // A plane is defined with the new positions. The plane is displayed
    // using a square [Scene](SceneManagement.Scene.html) example.  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Vector3](Vector3.html)[] positions;
        private [GameObject](GameObject.html)[] gameObjects;
        private int count = 7;
        private float timer = 999999f;
        private [Vector3](Vector3.html) position;  
      
        void Awake()
        {
            // Generate an array of GameObjects.  Use these to show where the
            // positions are based.
            gameObjects = new [GameObject](GameObject.html)[count];
            for (int i = 0; i < count; i++)
            {
                gameObjects[i] = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
                gameObjects[i].transform.localScale = new [Vector3](Vector3.html)(0.1f, 0.1f, 0.1f);
                gameObjects[i].name = "GO" + i.ToString();
            }
            positions = new [Vector3](Vector3.html)[count];  
      
            // Place the [Camera](Camera.html) in a sensible location.
            Camera.main.transform.position = new [Vector3](Vector3.html)(2.0f, 1.4f, 2.0f);
            Camera.main.transform.localEulerAngles = new [Vector3](Vector3.html)(26.0f, -135.0f, 0.0f);
        }  
      
        private [Plane](Plane.html) plane;
        void [Update](PlayerLoop.Update.html)()
        {
            // Compute positions of the 7 positions.
            if (timer > 5.0f) // True in first call.
            {
                // Generate an array of positions.
                MovePositions(count);  
      
                // Now find a plane passing through the positions.
                [GeometryUtility.TryCreatePlaneFromPolygon](GeometryUtility.TryCreatePlaneFromPolygon.html)(positions, out plane);  
      
                timer = 0.0f;
            }  
      
            DrawPlane([Vector3.zero](Vector3-zero.html), plane.normal);
            timer += [Time.deltaTime](Time-deltaTime.html);
        }  
      
        // Move the positions.
        void MovePositions(int count)
        {
            for (int i = 0; i < count; i++)
            {
                positions[i] = new [Vector3](Vector3.html)([Random.Range](Random.Range.html)(-1.0f, 1.0f), [Random.Range](Random.Range.html)(-0.5f, 0.5f), [Random.Range](Random.Range.html)(-1.0f, 1.0f));
                gameObjects[i].transform.position = positions[i];
            }
        }  
      
        // Generate and display a square that passes through the positions.
        // This only works in the [Scene](SceneManagement.Scene.html) view.
        void DrawPlane([Vector3](Vector3.html) position, [Vector3](Vector3.html) normal)
        {
            [Vector3](Vector3.html) v3;  
      
            if (normal.normalized != [Vector3.forward](Vector3-forward.html))
            {
                v3 = [Vector3.Cross](Vector3.Cross.html)(normal, [Vector3.forward](Vector3-forward.html)).normalized * normal.magnitude;
            }
            else
            {
                v3 = [Vector3.Cross](Vector3.Cross.html)(normal, [Vector3.up](Vector3-up.html)).normalized * normal.magnitude;
            }  
      
            // View the square and normal.
            [Vector3](Vector3.html) corner0 = position + v3;
            [Vector3](Vector3.html) corner2 = position - v3;
            [Quaternion](Quaternion.html) q = [Quaternion.AngleAxis](Quaternion.AngleAxis.html)(90.0f, normal);
            v3 = q * v3;
            [Vector3](Vector3.html) corner1 = position + v3;
            [Vector3](Vector3.html) corner3 = position - v3;  
      
            [Debug.DrawLine](Debug.DrawLine.html)(corner0, corner2, [Color.yellow](Color-yellow.html));
            [Debug.DrawLine](Debug.DrawLine.html)(corner1, corner3, [Color.yellow](Color-yellow.html));
            [Debug.DrawLine](Debug.DrawLine.html)(corner0, corner1, [Color.yellow](Color-yellow.html));
            [Debug.DrawLine](Debug.DrawLine.html)(corner1, corner2, [Color.yellow](Color-yellow.html));
            [Debug.DrawLine](Debug.DrawLine.html)(corner2, corner3, [Color.yellow](Color-yellow.html));
            [Debug.DrawLine](Debug.DrawLine.html)(corner3, corner0, [Color.yellow](Color-yellow.html));
            [Debug.DrawRay](Debug.DrawRay.html)(position, normal, [Color.green](Color-green.html));  
      
            // Draw lines between the positions.
            for (int i = 1; i < count; i++)
            {
                [Debug.DrawLine](Debug.DrawLine.html)(positions[i], positions[i - 1], [Color.blue](Color-blue.html));
            }
            [Debug.DrawLine](Debug.DrawLine.html)(positions[0], positions[count - 1], [Color.blue](Color-blue.html));
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

