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

#  [AssetDatabase](AssetDatabase.html).CreateAsset

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

public static void CreateAsset([Object](Object.html) asset, string path);

### Parameters

asset | Object to use in creating the asset.  
---|---  
path | Filesystem path for the new asset.  
  
### Description

Creates a new native Unity asset.

Use this method to create a native Unity asset. Native assets are those
created by Unity (either in the editor or via script), and are in Unity’s
serialized format.  
  
If an asset already exists the path you specify it will be overwritten with
your new asset. The path is relative to the project folder, for example:
"Assets/MyStuff/hello.mat".  
  
An asset file can contain multiple assets. After you create an asset file, you
can add more assets to the file using AssetDatabase.AddObjectToAsset.  
  
You cannot use this method to create an asset from a GameObject. To do this,
use the [PrefabUtility](PrefabUtility.html) class instead.  
  
Be aware that if you are adding multiple objects to an asset, the order in
which the objects are added does not matter. In other words, the first asset
added will not be special within the asset file, and there is no "root" asset
or object to which other assets are added to.  
  
Note: You must ensure that the path you provide uses a native asset extension.
For example, ".mat" for materials, ".cubemap" for cubemaps, ".GUISkin" for
skins, ".anim" for animations and ".asset" for arbitrary other assets. The
full list of native asset extensions can be found [here under the details for
NativeFormatImporter](../Manual/AssetDatabaseRefreshing.html). This method is
not intended for creating non-native assets, such as text files or image
files.  
  
Note: You cannot create assets inside the streaming assets folder
(Assets/StreamingAssets).  
  
Note: You should not create assets during import, for example from within a
ScriptedImporter or Postprocessor. Doing so can prevent the import process
from producing consistent (deterministic) results. See [Importer
Consistency](../Manual/ImporterConsistency.html) for more information.  
  
_This method reports an error in the console if you use an incorrect
extension, or if you try to create an asset in the streaming assets folder.
These errors will become exceptions in a future release of Unity._  
  
_This method reports a warning in the console if used during an import, but
this will become an exception in a future release of Unity._

    
    
    using UnityEngine;
    using [UnityEditor](UnityEditor.html);  
      
    public class CreateMaterialExample : [MonoBehaviour](MonoBehaviour.html)
    {
        [[MenuItem](MenuItem.html)("[GameObject](GameObject.html)/Create [Material](Material.html)")]
        static void CreateMaterial()
        {
            // Create a simple material asset  
      
            [Material](Material.html) material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Specular"));
            [AssetDatabase.CreateAsset](AssetDatabase.CreateAsset.html)(material, "Assets/MyMaterial.mat");  
      
            // Print the path of the created asset
            [Debug.Log](Debug.Log.html)([AssetDatabase.GetAssetPath](AssetDatabase.GetAssetPath.html)(material));
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

