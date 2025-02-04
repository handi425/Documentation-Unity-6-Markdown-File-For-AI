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

#  [EditorApplication](EditorApplication.html).timeSinceStartup

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

public static double timeSinceStartup;

### Description

The time since the editor was started. (Read Only)

This property contains the time since the editor was started, in seconds.
Unlike [Time.realtimeSinceStartup](Time-realtimeSinceStartup.html), this is
not reset when starting play mode.  
  
Additional resources: [Time.realtimeSinceStartup](Time-
realtimeSinceStartup.html)  
  
![](../StaticFiles/ScriptRefImages/SimpleAutoSave.png)  
_Simple Editor Window that saves each 300 seconds the current Scene._

    
    
    // Simple editor window that autosaves the working [Scene](SceneManagement.Scene.html)
    // Make sure to have this window opened to be able to execute the auto save.  
      
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine.SceneManagement;
    using UnityEditor.SceneManagement;  
      
    public class SimpleAutoSave : [EditorWindow](EditorWindow.html)
    {
        static float saveTime = 300.0f;
        static double nextSave = 0;  
      
        static int autoSaveLabel = 1;  
      
        [[MenuItem](MenuItem.html)("Examples/Simple autoSave")]
        static void Init()
        {
            SimpleAutoSave window = (SimpleAutoSave)GetWindowWithRect(
                typeof(SimpleAutoSave),
                new [Rect](Rect.html)(0, 0, 160, 60));
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(10, 10, 80, 20), "Save Each:");
            [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(80, 10, 80, 20), saveTime + " secs");  
      
            double timeToSave = nextSave - [EditorApplication.timeSinceStartup](EditorApplication-timeSinceStartup.html);  
      
    
            [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(10, 30, 80, 20), "Next Save:");
            [EditorGUI.LabelField](EditorGUI.LabelField.html)(new [Rect](Rect.html)(80, 30, 80, 20), timeToSave.ToString("N1") + " secs");  
      
            this.Repaint();  
      
            // when time has reach zero then save the [Scene](SceneManagement.Scene.html)
            if ([EditorApplication.timeSinceStartup](EditorApplication-timeSinceStartup.html) > nextSave)
            {
                [Scene](SceneManagement.Scene.html) scene = [SceneManager.GetActiveScene](SceneManagement.SceneManager.GetActiveScene.html)();
                string name = scene.name + autoSaveLabel;  
      
                [EditorSceneManager.SaveScene](SceneManagement.EditorSceneManager.SaveScene.html)(scene, "Assets/wibble/" + name + ".unity", true);
                autoSaveLabel = autoSaveLabel + 1;
                nextSave = [EditorApplication.timeSinceStartup](EditorApplication-timeSinceStartup.html) + saveTime;  
      
                [Debug.Log](Debug.Log.html)("Saved [Scene](SceneManagement.Scene.html): " + name);
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

