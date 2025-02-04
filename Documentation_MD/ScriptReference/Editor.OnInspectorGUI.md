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

#  [Editor](Editor.html).OnInspectorGUI

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

public void OnInspectorGUI();

### Description

Implement this function to make a custom inspector.

Inside this function you can add your own custom IMGUI based GUI for the
inspector of a specific object class.  
  
**Note:** This function has to be overridden in order to work.  
  
Additional resources:
[Editor.DrawDefaultInspector](Editor.DrawDefaultInspector.html).  
  
The example below shows how a custom label can be created by using `override`:

    
    
    using UnityEngine;
    using System.Collections;
    using [UnityEditor](UnityEditor.html);  
      
    // Creates a custom [Label](UIElements.Label.html) on the inspector for all the scripts named ScriptName
    // Make sure you have a ScriptName script in your
    // project, else this will not work.
    [[CustomEditor](CustomEditor.html)(typeof(ScriptName))]
    public class TestOnInspector : [Editor](Editor.html)
    {
        public override void OnInspectorGUI()
        {
            [GUILayout.Label](GUILayout.Label.html) ("This is a [Label](UIElements.Label.html) in a Custom [Editor](Editor.html)");
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

