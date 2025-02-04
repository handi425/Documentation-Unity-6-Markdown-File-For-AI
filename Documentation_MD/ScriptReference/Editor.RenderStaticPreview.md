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

#  [Editor](Editor.html).RenderStaticPreview

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

public [Texture2D](Texture2D.html) RenderStaticPreview(string assetPath,
Object[] subAssets, int width, int height);

### Parameters

assetPath | The asset to operate on.  
---|---  
subAssets | An array of all Assets at assetPath.  
width | Width of the created texture.  
height | Height of the created texture.  
  
### Returns

**Texture2D** Generated texture or null.

### Description

Override this method if you want to render a static preview.

When overridden [RenderStaticPreview](Editor.RenderStaticPreview.html) can be
used to render a list of assets converted into a single texture. This function
will need user supplied source code that can merge the assets together. The
size of the create texture can be supplied by the provided width and height.  
If null is returned the builtin icon for the class type is used.

    
    
    // Render the provided asset texture into an Inspector thumbnail.
    using UnityEngine;
    using System.Collections;
    using [UnityEditor](UnityEditor.html);  
      
    using System.IO;  
      
    public class Example : [ScriptableObject](ScriptableObject.html)
    {
        public [Texture2D](Texture2D.html) PreviewIcon;
    }  
      
    
    [[CustomEditor](CustomEditor.html)(typeof(Example))]
    public class ExampleEditor : UnityEditor.Editor
    {
        public static void CreateAsset<Example>() where Example : [ScriptableObject](ScriptableObject.html)
        {
            Example asset = [ScriptableObject.CreateInstance](ScriptableObject.CreateInstance.html)<Example>();  
      
            string path = [AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)([Selection.activeObject](Selection-activeObject.html));  
      
            if (path == "")
            {
                path = "Assets";
            }
            else if (Path.GetExtension(path) != "")
            {
                path = path.Replace(Path.GetFileName([AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)([Selection.activeObject](Selection-activeObject.html))), "");
            }  
      
            string assetPathAndName = [AssetDatabase.GenerateUniqueAssetPath](AssetDatabase.GenerateUniqueAssetPath.html)(path + "/New " + typeof(Example).ToString() + ".asset");  
      
            [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(asset, assetPathAndName);
            [AssetDatabase.SaveAssets](AssetDatabase.SaveAssets.html)();
            [AssetDatabase.Refresh](AssetDatabase.Refresh.html)();
            [EditorUtility.FocusProjectWindow](EditorUtility.FocusProjectWindow.html)();
            [Selection.activeObject](Selection-activeObject.html) = asset;
        }  
      
        [[MenuItem](MenuItem.html)("Examples/RenderStaticPreview example")]
        public static void CreateAsset()
        {
            CreateAsset<Example>();
        }  
      
        public override void OnInspectorGUI()
        {
            Example e = (Example)target;  
      
            [EditorGUI.BeginChangeCheck](EditorGUI.BeginChangeCheck.html)();  
      
            // Example has a single arg called PreviewIcon which is a [Texture2D](Texture2D.html)
            e.PreviewIcon = ([Texture2D](Texture2D.html))
                    [EditorGUILayout.ObjectField](EditorGUILayout.ObjectField.html)(
                        "Thumbnail",                    // string
                        e.PreviewIcon,                  // [Texture2D](Texture2D.html)
                        typeof([Texture2D](Texture2D.html)),              // [Texture2D](Texture2D.html) object, of course
                        false                           // allowSceneObjects
                    );  
      
            if ([EditorGUI.EndChangeCheck](EditorGUI.EndChangeCheck.html)())
            {
                [EditorUtility.SetDirty](EditorUtility.SetDirty.html)(e);
                [AssetDatabase.SaveAssets](AssetDatabase.SaveAssets.html)();
                Repaint();
            }
        }  
      
        public override [Texture2D](Texture2D.html) RenderStaticPreview(string assetPath, Object[] subAssets, int width, int height)
        {
            Example example = (Example)target;  
      
            if (example == null || example.PreviewIcon == null)
                return null;  
      
            // example.PreviewIcon must be a supported format: ARGB32, RGBA32, RGB24,
            // Alpha8 or one of float formats
            [Texture2D](Texture2D.html) tex = new [Texture2D](Texture2D.html) (width, height);
            [EditorUtility.CopySerialized](EditorUtility.CopySerialized.html) (example.PreviewIcon, tex);  
      
            return tex;
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

