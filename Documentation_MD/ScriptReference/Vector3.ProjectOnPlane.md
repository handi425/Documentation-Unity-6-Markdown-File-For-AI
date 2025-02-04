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

#  [Vector3](Vector3.html).ProjectOnPlane

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

public static [Vector3](Vector3.html) ProjectOnPlane([Vector3](Vector3.html)
vector, [Vector3](Vector3.html) planeNormal);

### Parameters

vector | The vector to project on the plane.  
---|---  
planeNormal | The normal which defines the plane to project on.  
  
### Returns

**Vector3** The orthogonal projection of `vector` on the plane.

### Description

Projects a vector onto a plane.

For a given plane described by `planeNormal` and a given vector `vector`,
[Vector3.ProjectOnPlane](Vector3.ProjectOnPlane.html) generates a new vector
orthogonal to `planeNormal` and parallel to the plane. Note: `planeNormal`
does not need to be normalized.  
  
![](../StaticFiles/ScriptRefImages/Vector3ProjectOnPlane.png)  
''The red line represents `vector`, the yellow line represents `planeNormal`,
and the blue line represents the projection of `vector` on the plane.''  
  
The script example below makes `Update` generate a `vector` position, and a
`planeNormal` normal. The
[Vector3.ProjectOnPlane](Vector3.ProjectOnPlane.html) static method receives
the arguments and returns the [Vector3](Vector3.html) position.

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;  
      
    // [Vector3.ProjectOnPlane](Vector3.ProjectOnPlane.html) - example  
      
    // Generate a random plane in xy. Show the position of a random
    // vector and a connection to the plane. The example shows nothing
    // in the Game view but uses [Update](PlayerLoop.Update.html)(). The script reference example
    // uses [Gizmos](Gizmos.html) to show the positions and axes in the [Scene](SceneManagement.Scene.html).  
      
    public class Example : [MonoBehaviour](MonoBehaviour.html)
    {
        private [Vector3](Vector3.html) vector, planeNormal;
        private [Vector3](Vector3.html) response;
        private float radians;
        private float degrees;
        private float timer = 12345.0f;  
      
        // Generate the values for all the examples.
        // Change the example every two seconds.
        void [Update](PlayerLoop.Update.html)()
        {
            if (timer > 2.0f)
            {
                // Generate a position inside xy space.
                vector = new [Vector3](Vector3.html)([Random.Range](Random.Range.html)(-1.0f, 1.0f), [Random.Range](Random.Range.html)(-1.0f, 1.0f), 0.0f);  
      
                // Compute a normal from the plane through the origin.
                degrees = [Random.Range](Random.Range.html)(-45.0f, 45.0f);
                radians = degrees * [Mathf.Deg2Rad](Mathf.Deg2Rad.html);
                planeNormal = new [Vector3](Vector3.html)([Mathf.Cos](Mathf.Cos.html)(radians), [Mathf.Sin](Mathf.Sin.html)(radians), 0.0f);  
      
                // Obtain the ProjectOnPlane result.
                response = [Vector3.ProjectOnPlane](Vector3.ProjectOnPlane.html)(vector, planeNormal);  
      
                // Reset the timer.
                timer = 0.0f;
            }
            timer += [Time.deltaTime](Time-deltaTime.html);
        }  
      
        // Show a [Scene](SceneManagement.Scene.html) view example.
        void OnDrawGizmosSelected()
        {
            // Left/right and up/down axes.
            [Gizmos.color](Gizmos-color.html) = [Color.white](Color-white.html);
            [Gizmos.DrawLine](Gizmos.DrawLine.html)(transform.position - new [Vector3](Vector3.html)(2.25f, 0, 0), transform.position + new [Vector3](Vector3.html)(2.25f, 0, 0));
            [Gizmos.DrawLine](Gizmos.DrawLine.html)(transform.position - new [Vector3](Vector3.html)(0, 1.75f, 0), transform.position + new [Vector3](Vector3.html)(0, 1.75f, 0));  
      
            // [Display](Display.html) the plane.
            [Gizmos.color](Gizmos-color.html) = [Color.green](Color-green.html);
            [Vector3](Vector3.html) angle = new [Vector3](Vector3.html)(-1.75f * [Mathf.Sin](Mathf.Sin.html)(radians), 1.75f * [Mathf.Cos](Mathf.Cos.html)(radians), 0.0f);
            [Gizmos.DrawLine](Gizmos.DrawLine.html)(transform.position - angle, transform.position + angle);  
      
            // Show the projection on the plane as a blue line.
            [Gizmos.color](Gizmos-color.html) = [Color.blue](Color-blue.html);
            [Gizmos.DrawLine](Gizmos.DrawLine.html)([Vector3.zero](Vector3-zero.html), response);
            [Gizmos.DrawSphere](Gizmos.DrawSphere.html)(response, 0.05f);  
      
            // Show the vector perpendicular to the plane in yellow
            [Gizmos.color](Gizmos-color.html) = [Color.yellow](Color-yellow.html);
            [Gizmos.DrawLine](Gizmos.DrawLine.html)(vector, response);  
      
            // Now show the input position.
            [Gizmos.color](Gizmos-color.html) = [Color.red](Color-red.html);
            [Gizmos.DrawSphere](Gizmos.DrawSphere.html)(vector, 0.05f);
            [Gizmos.DrawLine](Gizmos.DrawLine.html)([Vector3.zero](Vector3-zero.html), vector);
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

