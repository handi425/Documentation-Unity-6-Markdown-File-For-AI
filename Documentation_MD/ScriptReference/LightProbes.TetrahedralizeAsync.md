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

#  [LightProbes](LightProbes.html).TetrahedralizeAsync

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

public static void TetrahedralizeAsync();

### Description

Asynchronously tetrahedralize all currently loaded LightProbe positions.

Call this function to asynchronously calculate a Delaunay tetrahedralization
of all currently loaded LightProbe positions, and update the
[LightProbes](LightProbes.html) object with the result. Note that Unity does
not raise an event when this asynchronous method completes.  
  
Call this method after you load a Scene with
[LoadSceneMode.Additive](SceneManagement.LoadSceneMode.Additive.html), or
unload a Scene with
[SceneManager.UnloadSceneAsync](SceneManagement.SceneManager.UnloadSceneAsync.html).
Note that updating the tetrahedral tessellation is CPU-intensive. For more
information, see [Light Probes and Scene loading](../Manual/light-probes-and-
scene-loading.html).

    
    
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class TetrahedralizeAsyncExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            // Additively load a [Scene](SceneManagement.Scene.html) containing light probes
            [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("ExampleScene", [LoadSceneMode.Additive](SceneManagement.LoadSceneMode.Additive.html));  
      
            // Force Unity to asynchronously regenerate the tetrahedral tesselation for all loaded Scenes
            [LightProbes.TetrahedralizeAsync](LightProbes.TetrahedralizeAsync.html)();
        }
    }
    

Additional resources:
[LightProbes.Tetrahedralize](LightProbes.Tetrahedralize.html), [Light Probes
in the Unity Manual](../Manual/LightProbes.html),
[Lightmapping.Tetrahedralize](Lightmapping.Tetrahedralize.html).

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

