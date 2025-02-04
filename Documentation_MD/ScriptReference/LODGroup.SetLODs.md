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

#  [LODGroup](LODGroup.html).SetLODs

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

[Switch to Manual](../Manual/class-LODGroup.html "Go to LODGroup Component in
the Manual")

## Declaration

public void SetLODs(LOD[] lods);

### Parameters

lods | The LODs to use for this group.  
---|---  
  
### Description

Set the LODs for the LOD group. This will remove any existing LODs configured
on the LODGroup.

    
    
    using UnityEngine;
    using System.Collections;  
      
    public class ExampleClass : [MonoBehaviour](MonoBehaviour.html)
    {
        public [LODGroup](LODGroup.html) group;  
      
        void Start()
        {
            // Programmatically create a [LOD](LOD.html) group and add [LOD](LOD.html) levels.
            // Create a [GUI](GUI.html) that allows for forcing a specific [LOD](LOD.html) level.
            group = gameObject.AddComponent<[LODGroup](LODGroup.html)>();  
      
            // Add 4 [LOD](LOD.html) levels
            [LOD](LOD.html)[] lods = new [LOD](LOD.html)[4];
            for (int i = 0; i < 4; i++)
            {
                [PrimitiveType](PrimitiveType.html) primType = [PrimitiveType.Cube](PrimitiveType.Cube.html);
                switch (i)
                {
                    case 1:
                        primType = [PrimitiveType.Capsule](PrimitiveType.Capsule.html);
                        break;
                    case 2:
                        primType = [PrimitiveType.Sphere](PrimitiveType.Sphere.html);
                        break;
                    case 3:
                        primType = [PrimitiveType.Cylinder](PrimitiveType.Cylinder.html);
                        break;
                }
                [GameObject](GameObject.html) go = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)(primType);
                go.transform.parent = gameObject.transform;
                [Renderer](Renderer.html)[] renderers = new [Renderer](Renderer.html)[1];
                renderers[0] = go.GetComponent<[Renderer](Renderer.html)>();
                lods[i] = new [LOD](LOD.html)(1.0F / (i + 2), renderers);
            }
            group.SetLODs(lods);
            group.RecalculateBounds();
        }  
      
        void OnGUI()
        {
            if ([GUILayout.Button](GUILayout.Button.html)("Enable / Disable"))
                group.enabled = !group.enabled;  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Default"))
                group.ForceLOD(-1);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Force 0"))
                group.ForceLOD(0);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Force 1"))
                group.ForceLOD(1);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Force 2"))
                group.ForceLOD(2);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Force 3"))
                group.ForceLOD(3);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Force 4"))
                group.ForceLOD(4);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Force 5"))
                group.ForceLOD(5);  
      
            if ([GUILayout.Button](GUILayout.Button.html)("Force 6"))
                group.ForceLOD(6);
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

