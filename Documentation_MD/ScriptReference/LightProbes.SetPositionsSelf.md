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

#  [LightProbes](LightProbes.html).SetPositionsSelf

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

public bool SetPositionsSelf(Vector3[] positions, bool
checkForDuplicatePositions);

### Parameters

checkForDuplicatePositions | Whether to check for duplicate light probe positions at the cost of performance.  
---|---  
positions | The positions to set.  
  
### Returns

**bool** `true` when the positions were successfully set. Otherwise `false`.

### Description

Sets the positions of the baked light probes stored in this `LightProbes`
object.

When you change the positions of baked light probes using this method, you
must call [LightProbes.Tetrahedralize](LightProbes.Tetrahedralize.html) or
[LightProbes.TetrahedralizeAsync](LightProbes.TetrahedralizeAsync.html) to
fully apply the changes.  
  
Setting duplicate light probe positions will lead to incorrect behavior, such
as black light probes appearing..  
  
The following script additively loads a scene containing baked light probes
and moves the probes:

    
    
    using System.Collections;
    using UnityEngine;
    using UnityEngine.SceneManagement;  
      
    public class MoveLightProbesExample : [MonoBehaviour](MonoBehaviour.html)
    {
        void Start()
        {
            StartCoroutine(LoadSceneAndMoveLightProbes());
        }  
      
        IEnumerator LoadSceneAndMoveLightProbes()
        {
            // Fully load a scene containing light probes additively.
            [Scene](SceneManagement.Scene.html) additiveScene = [SceneManager.LoadScene](SceneManagement.SceneManager.LoadScene.html)("AdditiveScene", new [LoadSceneParameters](SceneManagement.LoadSceneParameters.html)([LoadSceneMode.Additive](SceneManagement.LoadSceneMode.Additive.html)));
            yield return null;  
      
            // Get the light probes for the scene.
            [LightProbes](LightProbes.html) lightProbes = [LightProbes.GetInstantiatedLightProbesForScene](LightProbes.GetInstantiatedLightProbesForScene.html)(additiveScene);  
      
            // Move the light probes slightly.
            [Vector3](Vector3.html)[] positions = lightProbes.GetPositionsSelf();
            for (int i = 0; i < positions.Length; i++)
            {
                positions[i] += [Vector3.one](Vector3-one.html);
            }
            lightProbes.SetPositionsSelf(positions, true);  
      
            // Tetrahedralize to apply the changes to light probe positions.
            [LightProbes.TetrahedralizeAsync](LightProbes.TetrahedralizeAsync.html)();
        }
    }
    

Additional resources: [LightProbes.countSelf](LightProbes-countSelf.html).

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

