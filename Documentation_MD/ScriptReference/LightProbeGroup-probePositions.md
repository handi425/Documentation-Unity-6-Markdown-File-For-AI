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

#  [LightProbeGroup](LightProbeGroup.html).probePositions

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

[Switch to Manual](../Manual/class-LightProbeGroup.html "Go to LightProbeGroup
Component in the Manual")

public Vector3[] probePositions;

### Description

Editor only function to access and modify probe positions.

Probe positions are specified in local space relative to the parent object.  
  
At runtime this function will return an empty Vector3 array and setting it
will have no effect.

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class ExampleScript : [EditorWindow](EditorWindow.html)
    {
        private [LightProbeGroup](LightProbeGroup.html) lightProbes = null;  
      
        [[MenuItem](MenuItem.html)("Example/Set Probe Positions")]
        static void Init()
        {
            var window = GetWindowWithRect<ExampleScript>(new [Rect](Rect.html)(0, 0, 350, 50));
            window.Show();
        }  
      
        void OnGUI()
        {
            lightProbes = ([LightProbeGroup](LightProbeGroup.html))[EditorGUILayout.ObjectField](EditorGUILayout.ObjectField.html)(
                "Find Dependency",     // string
                lightProbes,       // Object
                typeof([LightProbeGroup](LightProbeGroup.html)),     // Type
                true);  
      
            if (lightProbes)
            {
                if ([GUILayout.Button](GUILayout.Button.html)("Set Probe Positions"))
                {
                    [Vector3](Vector3.html)[] positions = new [Vector3](Vector3.html)[4];
                    positions[0] = new [Vector3](Vector3.html)(0.0f, 0.0f, 0.0f);
                    positions[1] = new [Vector3](Vector3.html)(1.0f, 0.0f, 0.0f);
                    positions[2] = new [Vector3](Vector3.html)(0.0f, 1.0f, 0.0f);
                    positions[3] = new [Vector3](Vector3.html)(1.0f, 1.0f, 1.0f);
                    lightProbes.probePositions = positions;
                }
            }
            else
            {
                [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Missing:", "Please select an object first!");
            }
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

