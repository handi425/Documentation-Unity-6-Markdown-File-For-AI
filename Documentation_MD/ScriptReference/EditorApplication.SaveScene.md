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

**Method group is Obsolete**  

#  [EditorApplication](EditorApplication.html).SaveScene

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

**Obsolete** Use EditorSceneManager.SaveScene.

## Declaration

public static bool SaveScene();

**Obsolete** Use EditorSceneManager.SaveScene.

## Declaration

public static bool SaveScene(string path);

**Obsolete** Use EditorSceneManager.SaveScene.

## Declaration

public static bool SaveScene(string path, bool saveAsCopy);

### Parameters

path | The file path to save at. If empty, the current open Scene will be overwritten, or if never saved before, a save dialog is shown.  
---|---  
saveAsCopy | If set to `true`, the Scene will be saved without changing the [currentScene](EditorApplication-currentScene.html) and without clearing the unsaved changes marker.  
  
### Returns

**bool** True if the save succeeded, otherwise false.

### Description

Save the open Scene.

All paths are relative to the project folder, such as:
"Assets/MyScenes/MyScene.unity". Folders specified in the path must already
exist before calling the function. If no path is specified, the path of the
current open Scene is used, except if it was never saved before, in which case
a save dialog is shown.  
  
The function returns `false` if the save failed. This can happen if the
specified path is invalid or if the user cancels in the case of a save dialog.  
  
When calling the function, the unsaved changes marker is cleared, just as when
saving using the file menu. (On Windows, the unsaved changes marker is an
asterix after the file name in the window title. On macOS it's a dot inside
the red close button of the window.) When a path is specified, the
[currentScene](EditorApplication-currentScene.html) is also changed to be the
specified asset.  
  
When `saveAsCopy` is set to `true` however, neither the
[currentScene](EditorApplication-currentScene.html) or the unsaved changes
marker is changed.  
  
Additional resources: [currentScene](EditorApplication-currentScene.html).  
  
![](../StaticFiles/ScriptRefImages/SimpleAutoSave.png)  
_Simple Editor Window that saves each 300 seconds the current Scene._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class SimpleAutoSave : [EditorWindow](EditorWindow.html)
    {
        float saveTime = 300f;
        float nextSave = 0f;  
      
        [[MenuItem](MenuItem.html)("Example/Simple autoSave")]
        static void Init()
        {
            SimpleAutoSave window = [EditorWindow.GetWindowWithRect](EditorWindow.GetWindowWithRect.html)<SimpleAutoSave>(new [Rect](Rect.html)(0, 0, 165, 40), true);
            window.Show();
        }  
      
        void OnGUI()
        {
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Save Each:", saveTime + " Secs");
            int timeToSave = (int)(nextSave - [EditorApplication.timeSinceStartup](EditorApplication-timeSinceStartup.html));
            [EditorGUILayout.LabelField](EditorGUILayout.LabelField.html)("Next Save:", timeToSave.ToString() + " Sec");
            this.Repaint();  
      
            if ([EditorApplication.timeSinceStartup](EditorApplication-timeSinceStartup.html) > nextSave)
            {
                string[] path = EditorApplication.currentScene.Split(char.Parse("/"));
                path[path.Length - 1] = "AutoSave_" + path[path.Length - 1];
                EditorApplication.SaveScene(string.Join("/", path), true);
                [Debug.Log](Debug.Log.html)("Saved [Scene](SceneManagement.Scene.html)");
                nextSave = (int)([EditorApplication.timeSinceStartup](EditorApplication-timeSinceStartup.html) + saveTime);
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

