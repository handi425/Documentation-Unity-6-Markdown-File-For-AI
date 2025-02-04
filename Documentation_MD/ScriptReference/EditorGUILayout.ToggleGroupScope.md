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

# ToggleGroupScope

class in UnityEditor

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

### Description

Begin a vertical group with a toggle to enable or disable all the controls
within at once.

Additional resources:
[BeginToggleGroup](EditorGUILayout.BeginToggleGroup.html).  
  
![](../StaticFiles/ScriptRefImages/Aligner.png)  
_Align position/rotation/scale of the selected GameObjects._

    
    
    // C# Example
    // Simple script that lets you align GameObjects
    // position/rotation/scale wise with the selected active transform  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class Aligner : [EditorWindow](EditorWindow.html)
    {
        bool[] pos = new bool[3] { true, true, true };
        bool[] rot = new bool[3] { true, true, true };
        bool[] scale = new bool[3] { true, true, true };  
      
        bool posGroupEnabled = true;
        bool rotGroupEnabled = true;
        bool scaleGroupEnabled = false;  
      
        void OnGUI()
        {
            using (var posGroup = new [EditorGUILayout.ToggleGroupScope](EditorGUILayout.ToggleGroupScope.html)("[Align](UIElements.Align.html) position", posGroupEnabled))
            {
                posGroupEnabled = posGroup.enabled;
                pos[0] = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("x", pos[0]);
                pos[1] = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("y", pos[1]);
                pos[2] = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("z", pos[2]);
            }  
      
            using (var rotGroup = new [EditorGUILayout.ToggleGroupScope](EditorGUILayout.ToggleGroupScope.html)("[Align](UIElements.Align.html) rotation", rotGroupEnabled))
            {
                rotGroupEnabled = rotGroup.enabled;
                rot[0] = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("x", rot[0]);
                rot[1] = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("y", rot[1]);
                rot[2] = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("z", rot[2]);
            }  
      
            using (var scaleGroup = new [EditorGUILayout.ToggleGroupScope](EditorGUILayout.ToggleGroupScope.html)("[Align](UIElements.Align.html) scale", scaleGroupEnabled))
            {
                scaleGroupEnabled = scaleGroup.enabled;
                scale[0] = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("x", scale[0]);
                scale[1] = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("y", scale[1]);
                scale[2] = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("z", scale[2]);
            }  
      
            [GUILayout.Space](GUILayout.Space.html)(30);
            if ([GUILayout.Button](GUILayout.Button.html)("[Align](UIElements.Align.html)!"))
                [Align](UIElements.Align.html)();
        }  
      
        void [Align](UIElements.Align.html)()
        {
            [Transform](Transform.html)[] transforms = [Selection.transforms](Selection-transforms.html);
            [Transform](Transform.html) activeTransform = [Selection.activeTransform](Selection-activeTransform.html);
            if (transforms.Length < 2)
            {
                [Debug.LogWarning](Debug.LogWarning.html)("Aligner: select at least two objects.");
                return;
            }
            for (int i = 0; i < transforms.Length; i++)
            {
                if (posGroupEnabled)
                {
                    [Vector3](Vector3.html) newPos;
                    newPos.x = pos[0] ?
                        activeTransform.position.x : transforms[i].position.x;
                    newPos.y = pos[1] ?
                        activeTransform.position.y : transforms[i].position.y;
                    newPos.z = pos[2] ?
                        activeTransform.position.z : transforms[i].position.z;
                    transforms[i].position = newPos;
                }
                if (rotGroupEnabled)
                {
                    [Vector3](Vector3.html) newRot;
                    newRot.x = rot[0] ?
                        activeTransform.rotation.eulerAngles.x : transforms[i].rotation.eulerAngles.x;
                    newRot.y = rot[1] ?
                        activeTransform.rotation.eulerAngles.y : transforms[i].rotation.eulerAngles.y;
                    newRot.z = rot[2] ?
                        activeTransform.rotation.eulerAngles.z : transforms[i].rotation.eulerAngles.z;
                    transforms[i].rotation = [Quaternion.Euler](Quaternion.Euler.html)(newRot);
                }
                if (scaleGroupEnabled)
                {
                    [Vector3](Vector3.html) newScale;
                    newScale.x = scale[0] ?
                        activeTransform.localScale.x : transforms[i].localScale.x;
                    newScale.y = scale[1] ?
                        activeTransform.localScale.y : transforms[i].localScale.y;
                    newScale.z = scale[2] ?
                        activeTransform.localScale.z : transforms[i].localScale.z;
                    transforms[i].localScale = newScale;
                }
            }
        }  
      
        [[MenuItem](MenuItem.html)("Examples/[Position](UIElements.Position.html)-Rotation-[Scale](UIElements.Scale.html) Aligner")]
        static void Init()
        {
            Aligner window = (Aligner)[EditorWindow.GetWindow](EditorWindow.GetWindow.html)(typeof(Aligner));
            window.Show();
        }
    }
    

### Properties

[enabled](EditorGUILayout.ToggleGroupScope-enabled.html)| The enabled state
selected by the user.  
---|---  
  
### Constructors

[EditorGUILayout.ToggleGroupScope](EditorGUILayout.ToggleGroupScope-
ctor.html)|  
---|---  
  
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

