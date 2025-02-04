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

#  [Mesh](Mesh.html).colors

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

public Color[] colors;

### Description

Vertex colors of the Mesh.

If no vertex colors are available, an empty array will be returned.

    
    
    // Sets the vertex color to be red at the y=0 and green at y=1.
    // (Note that most built-in Shaders don't display vertex colors. Use one that does, such as a [Particle](ParticleSystem.Particle.html) [Shader](Shader.html), to see vertex colors)  
      
    using UnityEngine;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            [Mesh](Mesh.html) mesh = GetComponent<[MeshFilter](MeshFilter.html)>().mesh;
            [Vector3](Vector3.html)[] vertices = mesh.vertices;  
      
            // create new colors array where the colors will be created.
            [Color](Color.html)[] colors = new [Color](Color.html)[vertices.Length];  
      
            for (int i = 0; i < vertices.Length; i++)
                colors[i] = [Color.Lerp](Color.Lerp.html)([Color.red](Color-red.html), [Color.green](Color-green.html), vertices[i].y);  
      
            // assign the array of colors to the [Mesh](Mesh.html).
            mesh.colors = colors;
        }
    }
    

For performance reasons, consider using [colors32](Mesh-colors32.html)
instead. This will avoid byte-to-float conversions in colors, and use less
temporary memory.

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

