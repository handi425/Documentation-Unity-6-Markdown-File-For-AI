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

#  [EditorSceneManager](SceneManagement.EditorSceneManager.html).SaveScene

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

public static bool
SaveScene([SceneManagement.Scene](SceneManagement.Scene.html) scene, string
dstScenePath = "", bool saveAsCopy = false);

### Parameters

scene | The Scene to be saved.  
---|---  
dstScenePath | The file path to save the Scene to. If the path is empty, the current open Scene is overwritten. If it has not yet been saved at all, a save dialog is shown.  
saveAsCopy | If set to true, the Scene is saved without changing the current Scene, and without clearing the unsaved changes marker.  
  
### Returns

**bool** True if the save succeeded, otherwise false.

### Description

Save a Scene.

All paths are relative to the project folder, such as:
"Assets/MyScenes/MyScene.unity". Folders specified in the path must already
exist before calling the function. If no path is specified, the path of the
current open Scene is used, except if it was never saved before, in which case
a save dialog is shown.  
  
The function returns false if the save failed. This can happen if the
specified path is invalid or if the user cancels in the case of a save dialog.  
  
Additional resources: EditorSceneManager.GetActiveScene  
  
Example: ![](../StaticFiles/ScriptRefImages/SimpleAutoSave.png)  
_Simple Editor Window that saves each 300 seconds the current Scene._  
  
**Note:** This saves the Scene whether it is marked dirty or not.

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using System.Collections;
    using UnityEditor.SceneManagement;  
      
    public class SimpleAutoSave : [EditorWindow](EditorWindow.html)
    {
        public float saveTime = 300;
        public float nextSave = 0;
        [[MenuItem](MenuItem.html)("Example/Simple autoSave")]
        static void Init()
        {
            SimpleAutoSave window = (SimpleAutoSave)[EditorWindow.GetWindowWithRect](EditorWindow.GetWindowWithRect.html)(typeof(SimpleAutoSave), new [Rect](Rect.html)(0, 0, 200, 50));
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Save Each:", saveTime + " Secs");
            float timeToSave = nextSave - (float)[EditorApplication.timeSinceStartup](EditorApplication-timeSinceStartup.html);
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Next Save:", timeToSave.ToString() + " Sec");
            Repaint();
            if ([EditorApplication.timeSinceStartup](EditorApplication-timeSinceStartup.html) > nextSave)
            {
                string[] path = EditorSceneManager.GetActiveScene().path.Split(char.Parse("/"));
                path[path.Length - 1] = "AutoSave_" + path[path.Length - 1];
                bool saveOK = [EditorSceneManager.SaveScene](SceneManagement.EditorSceneManager.SaveScene.html)(EditorSceneManager.GetActiveScene(), string.Join("/", path));
                [Debug.Log](Debug.Log.html)("Saved [Scene](SceneManagement.Scene.html) " + (saveOK ? "OK" : "[Error](PackageManager.Error.html)!"));
                nextSave = (float)[EditorApplication.timeSinceStartup](EditorApplication-timeSinceStartup.html) + saveTime;
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

