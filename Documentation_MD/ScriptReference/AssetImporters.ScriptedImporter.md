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

# ScriptedImporter

class in UnityEditor.AssetImporters

/

Inherits from:[AssetImporter](AssetImporter.html)

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

Abstract base class for custom Asset importers.

Scripted importers are scripts that are associated with specific file
extensions. They are invoked by Unity's Asset pipeline to convert the contents
of associated files into Assets.  
  
Use the
[ScriptedImporterAttribute](AssetImporters.ScriptedImporterAttribute.html)
class to register custom importers with the Asset pipeline.  
  
The C# fields of a ScriptedImporter are serialized, exactly like fields on a
MonoBehaviour. See [Script Serialization](../Manual/script-serialization.html)
for details. You can see these properties in the Inspector and use them to
control the behaviour of the importer for each asset. To programmatically
access the value of an asset's properties, use
[AssetImporter.GetAtPath](AssetImporter.GetAtPath.html) and type cast the
return value to the correct class derived from ScriptedImporter. After
changing values, trigger a fresh import by calling
[EditorUtility.SetDirty](EditorUtility.SetDirty.html) and then
[AssetImporter.SaveAndReimport](AssetImporter.SaveAndReimport.html).

    
    
    using UnityEngine;
    using UnityEditor.AssetImporters;
    using System.IO;  
      
    [[ScriptedImporter](AssetImporters.ScriptedImporter.html)(1, "cube")]
    public class CubeImporter : [ScriptedImporter](AssetImporters.ScriptedImporter.html)
    {
        public float m_Scale = 1;  
      
        public override void OnImportAsset([AssetImportContext](AssetImporters.AssetImportContext.html) ctx)
        {
            var cube = [GameObject.CreatePrimitive](GameObject.CreatePrimitive.html)([PrimitiveType.Cube](PrimitiveType.Cube.html));
            var position = [JsonUtility.FromJson](JsonUtility.FromJson.html)<[Vector3](Vector3.html)>(File.ReadAllText(ctx.assetPath));  
      
            cube.transform.position = position;
            cube.transform.localScale = new [Vector3](Vector3.html)(m_Scale, m_Scale, m_Scale);  
      
            // 'cube' is a [GameObject](GameObject.html) and will be automatically converted into a Prefab
            // (Only the 'Main [Asset](VersionControl.Asset.html)' is eligible to become a Prefab.)
            ctx.AddObjectToAsset("main obj", cube);
            ctx.SetMainObject(cube);  
      
            var material = new [Material](Material.html)([Shader.Find](Shader.Find.html)("Standard"));
            material.color = [Color.red](Color-red.html);  
      
            // Assets must be assigned a unique identifier string consistent across imports
            ctx.AddObjectToAsset("my [Material](Material.html)", material);  
      
            // Assets that are not passed into the context as import outputs must be destroyed
            var tempMesh = new [Mesh](Mesh.html)();
            DestroyImmediate(tempMesh);
        }
    }
    

### Public Methods

[OnImportAsset](AssetImporters.ScriptedImporter.OnImportAsset.html)| This
method must by overriden by the derived class and is called by the Asset
pipeline to import files.  
---|---  
[SupportsRemappedAssetType](AssetImporters.ScriptedImporter.SupportsRemappedAssetType.html)|
Override this method if your ScriptedImporter supports remapping specific
asset types.  
  
### Messages

[GatherDependenciesFromSourceFile](AssetImporters.ScriptedImporter.GatherDependenciesFromSourceFile.html)|
A static callback that you can implement to set up artifact dependencies to
other Assets, and optimize the order your assets are imported.  
---|---  
[OnValidate](AssetImporters.ScriptedImporter.OnValidate.html)| This function
is called when the importer is loaded or a value is changed in the Inspector.  
[Reset](AssetImporters.ScriptedImporter.Reset.html)| Reset to default values.  
  
### Inherited Members

### Properties

[assetBundleName](AssetImporter-assetBundleName.html)| Get or set the
AssetBundle name.  
---|---  
[assetBundleVariant](AssetImporter-assetBundleVariant.html)| Get or set the
AssetBundle variant.  
[assetPath](AssetImporter-assetPath.html)| The path name of the asset for this
importer. (Read Only)  
[importSettingsMissing](AssetImporter-importSettingsMissing.html)| The value
is true when no meta file is provided with the imported asset.  
[userData](AssetImporter-userData.html)| Get or set any user data.  
[hideFlags](Object-hideFlags.html)| Should the object be hidden, saved with
the Scene or modifiable by the user?  
[name](Object-name.html)| The name of the object.  
  
### Public Methods

[AddRemap](AssetImporter.AddRemap.html)| Map a sub-asset from an imported
asset (such as an FBX file) to an external Asset of the same type.  
---|---  
[GetExternalObjectMap](AssetImporter.GetExternalObjectMap.html)| Gets a copy
of the external object map used by the AssetImporter.  
[RemoveRemap](AssetImporter.RemoveRemap.html)| Removes an item from the map of
external objects.  
[SaveAndReimport](AssetImporter.SaveAndReimport.html)| Save asset importer
settings if asset importer is dirty.  
[SetAssetBundleNameAndVariant](AssetImporter.SetAssetBundleNameAndVariant.html)|
Set the AssetBundle name and variant.  
[GetInstanceID](Object.GetInstanceID.html)| Gets the instance ID of the
object.  
[ToString](Object.ToString.html)| Returns the name of the object.  
  
### Static Methods

[GetAtPath](AssetImporter.GetAtPath.html)| Retrieves the asset importer for
the asset at path.  
---|---  
[GetImportLog](AssetImporter.GetImportLog.html)| Retrieves logs generated
during the import of the asset at path.  
[Destroy](Object.Destroy.html)| Removes a GameObject, component or asset.  
[DestroyImmediate](Object.DestroyImmediate.html)| Destroys the object obj
immediately. You are strongly recommended to use Destroy instead.  
[DontDestroyOnLoad](Object.DontDestroyOnLoad.html)| Do not destroy the target
Object when loading a new Scene.  
[FindAnyObjectByType](Object.FindAnyObjectByType.html)| Retrieves any active
loaded object of Type type.  
[FindFirstObjectByType](Object.FindFirstObjectByType.html)| Retrieves the
first active loaded object of Type type.  
[FindObjectsByType](Object.FindObjectsByType.html)| Retrieves a list of all
loaded objects of Type type.  
[Instantiate](Object.Instantiate.html)| Clones the object original and returns
the clone.  
[InstantiateAsync](Object.InstantiateAsync.html)| Captures a snapshot of the
original object (that must be related to some GameObject) and returns the
AsyncInstantiateOperation.  
  
### Operators

[bool](Object-operator_Object.html)| Does the object exist?  
---|---  
[operator !=](Object-operator_ne.html)| Compares if two objects refer to a
different object.  
[operator ==](Object-operator_eq.html)| Compares two object references to see
if they refer to the same object.  
  
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

