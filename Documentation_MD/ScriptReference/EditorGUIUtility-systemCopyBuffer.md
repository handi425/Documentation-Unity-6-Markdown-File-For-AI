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

#  [EditorGUIUtility](EditorGUIUtility.html).systemCopyBuffer

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

public static string systemCopyBuffer;

### Description

The system copy buffer.

Use this to make Copy and Paste work for your own application. The
[systemCopyBuffer](EditorGUIUtility-systemCopyBuffer.html) captures any text
that is selected on the machine. This does not specifically have to be text
that is selected in Unity. Reading and writing
[systemCopyBuffer](EditorGUIUtility-systemCopyBuffer.html) is possible.
![](../StaticFiles/ScriptRefImages/EditorGUIUtilitySystemCopyBuffer.png)  
_Have more than 1 saved "copy" command._

    
    
    // Example that shows up to 5 strings.  These strings are captured from Copy
    // commands on the machine.  The Current buffer at the bottom of the window shows whatever string
    // is copied.  The string can be copied to one of the five Save rows when the Load toggle is
    // five Save rows when the Load toggle is off and one of the horizontal buttons is pressed.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SystemCopyBufferExample : [EditorWindow](EditorWindow.html)
    {
        string[] savedCopies = new string[5];
        bool load = false;  
      
        [[MenuItem](MenuItem.html)("Examples/Example showing systemCopyBuffer")]
        static void systemCopyBufferExample()
        {
            SystemCopyBufferExample window =
                [EditorWindow.GetWindow](EditorWindow.GetWindow.html)<SystemCopyBufferExample>();
            window.Show();
        }  
      
        void OnGUI()
        {
            load = [EditorGUILayout.Toggle](EditorGUILayout.Toggle.html)("Load:", load);  
      
            [EditorGUILayout.BeginHorizontal](EditorGUILayout.BeginHorizontal.html)();
            for (int i = 0; i < savedCopies.Length; i++)
                if ([GUILayout.Button](GUILayout.Button.html)(i.ToString()))
                    if (load)
                        [EditorGUIUtility.systemCopyBuffer](EditorGUIUtility-systemCopyBuffer.html) = savedCopies[i];
                    else
                        savedCopies[i] = [EditorGUIUtility.systemCopyBuffer](EditorGUIUtility-systemCopyBuffer.html);
            [EditorGUILayout.EndHorizontal](EditorGUILayout.EndHorizontal.html)();  
      
            for (int j = 0; j < savedCopies.Length; j++)
                [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Saved " + j, savedCopies[j]);  
      
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Current buffer:", [EditorGUIUtility.systemCopyBuffer](EditorGUIUtility-systemCopyBuffer.html));
            if ([GUILayout.Button](GUILayout.Button.html)("Clear all saves"))
                for (int s = 0; s < savedCopies.Length; s++)
                    savedCopies[s] = "";
        }  
      
        void OnInspectorUpdate()
        {
            this.Repaint();
        }
    }
    

**Note:** iOS and Android do not support this feature.

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

