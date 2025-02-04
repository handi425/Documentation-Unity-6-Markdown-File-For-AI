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

#  [Mesh](Mesh.html).normals

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

[Switch to Manual](../Manual/class-Mesh.html "Go to Mesh Component in the
Manual")

public Vector3[] normals;

### Description

The normals of the Mesh.

If the Mesh contains no normals, an empty array is returned.

    
    
    // [Rotate](UIElements.Rotate.html) the normals by speed every frame  
      
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        float speed = 100.0f;  
      
        // [Update](PlayerLoop.Update.html) is called once per frame
        void [Update](PlayerLoop.Update.html)()
        {
            // obtain the normals from the [Mesh](Mesh.html)
            [Mesh](Mesh.html) mesh = GetComponent<[MeshFilter](MeshFilter.html)>().mesh;
            [Vector3](Vector3.html)[] normals = mesh.normals;  
      
            // edit the normals in an external array
            [Quaternion](Quaternion.html) rotation = [Quaternion.AngleAxis](Quaternion.AngleAxis.html)([Time.deltaTime](Time-deltaTime.html) * speed, [Vector3.up](Vector3-up.html));
            for (int i = 0; i < normals.Length; i++)
                normals[i] = rotation * normals[i];  
      
            // assign the array of normals to the mesh
            mesh.normals = normals;
        }
    }
    

**Note:** To make changes to the [normals](Mesh-normals.html) it is important
to copy the normals from the [Mesh](Mesh.html). Once the [normals](Mesh-
normals.html) have been copied and changed the [normals](Mesh-normals.html)
can be reassigned back to the [Mesh](Mesh.html).

**Note:** [normals](Mesh-normals.html) are assigned to vertices, not
triangles.

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

