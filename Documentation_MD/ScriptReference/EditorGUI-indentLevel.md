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

#  [EditorGUI](EditorGUI.html).indentLevel

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

public static int indentLevel;

### Description

The indent level of the field labels.

[EditorGUILayout.LabelField](EditorGUILayout.LabelField.html) will display the
string given as an argument. This string can be displayed at a horizontal
position, and the position changed by [indentLevel](EditorGUI-
indentLevel.html). As [indentLevel](EditorGUI-indentLevel.html) increases the
labels will move right. Decreasing [indentLevel](EditorGUI-indentLevel.html)
will move labels to the left.  
![](../StaticFiles/ScriptRefImages/EditorGUIIndent.png)  
_Shows info of the selected object._

    
    
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class EditorGUIIndent : [EditorWindow](EditorWindow.html)
    {
        [[MenuItem](MenuItem.html)("Examples/indentLevel demo")]
        static void Init()
        {
            [EditorWindow](EditorWindow.html) window = GetWindow(typeof(EditorGUIIndent));
            window.position = new [Rect](Rect.html)(100, 100, 300, 150);
            window.Show();
        }  
      
        void OnGUI()
        {
            [Transform](Transform.html) obj = [Selection.activeTransform](Selection-activeTransform.html);
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Name:", obj ? obj.name : "Select an Object");  
      
            if (obj)
            {
                // Indent further the area of position and rotation
                [EditorGUI.indentLevel](EditorGUI-indentLevel.html)++;
                [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("[Position](UIElements.Position.html):", obj.position.ToString());
                [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Rotation:", obj.rotation.eulerAngles.ToString());  
      
                // Indent further again the area of rotation values
                [EditorGUI.indentLevel](EditorGUI-indentLevel.html)++;
                [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("X:", obj.rotation.x.ToString());
                [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Y:", obj.rotation.y.ToString());
                [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Z:", obj.rotation.z.ToString());
                [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("W:", obj.rotation.w.ToString());  
      
                // End of inner area
                [EditorGUI.indentLevel](EditorGUI-indentLevel.html)--;
                [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("[Scale](UIElements.Scale.html):", obj.localScale.ToString());  
      
                // End of area
                [EditorGUI.indentLevel](EditorGUI-indentLevel.html)--;
            }
        }
    }
    

To maximize future compatibility, do not make assumptions about what a
specific indent level means, but instead just increase or decrease by one
around blocks of controls that need to be more indented, as in the example
above.

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

