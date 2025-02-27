[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/sprite/sprite-editor/sprite-editor-data-provider-api.html)
  * [中文](/cn/current/Manual/sprite/sprite-editor/sprite-editor-data-provider-api.html)
  * [日本語](/ja/current/Manual/sprite/sprite-editor/sprite-editor-data-provider-api.html)
  * [한국어](/kr/current/Manual/sprite/sprite-editor/sprite-editor-data-provider-api.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/sprite/sprite-editor/sprite-editor-data-provider-api.html)
  * [中文](/cn/current/Manual/sprite/sprite-editor/sprite-editor-data-provider-api.html)
  * [日本語](/ja/current/Manual/sprite/sprite-editor/sprite-editor-data-provider-api.html)
  * [한국어](/kr/current/Manual/sprite/sprite-editor/sprite-editor-data-provider-api.html)

  * [Working in Unity](../../working-in-unity.html)
  * [2D in Unity](../../Unity2D.html)
  * [Sprites](../../sprite/sprite-landing.html)
  * [Sprite editor](../../sprite/sprite-editor/sprite-editor-landing.html)
  * Sprite Editor Data Provider API

[](../../sprite/sprite-editor/secondary-texture/delete-secondary-texture.html)

Delete a secondary texture

[](../../sprite/sorting-group/sorting-group-landing.html)

Sorting groups

# Sprite Editor Data Provider API

By using the **Sprite** A 2D graphic objects. If you are used to working in
3D, Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](../../sprite/sprite-landing.html)  
See in [Glossary](../../Glossary.html#Sprite) Editor Data Provider API, the
user can add, change and remove Sprite data in a custom importer or editor
tool. Refer to the code examples below to see how the API is applied.

**Important:** Some of the following examples contains an additional section
of code which is needed if you are using Unity 2021.2 or newer. If you are
using Unity 2021.1 or older, you should remove the indicated section to ensure
the code compiles properly.

## How to get ISpriteEditorDataProvider instances

The following examples show you how to use the API to get each respective
instance.

### Importer

    
    
    using UnityEditor;
    using UnityEditor.U2D.Sprites;
    using UnityEngine;
    
    public class MyAssetPostProcessor : AssetPostprocessor
    {
        private void OnPreprocessTexture()
        {
            var factory = new SpriteDataProviderFactories();
            factory.Init();
            var dataProvider = factory.GetSpriteEditorDataProviderFromObject(assetImporter);
            dataProvider.InitSpriteEditorDataProvider();
    
            /* Use the data provider */
    
            // Apply the changes made to the data provider
            dataProvider.Apply();
        }
    }
    

### Texture

    
    
    using UnityEditor;
    using UnityEditor.U2D.Sprites;
    using UnityEngine;
    
    public static class MyCustomTool
    {
        [MenuItem("Custom/Update Sprite Settings")]
        static void UpdateSettings()
        {
            foreach (var obj in Selection.objects)
            {
                if (obj is Texture2D)
                {
                    var factory = new SpriteDataProviderFactories();
                    factory.Init();
                    var dataProvider = factory.GetSpriteEditorDataProviderFromObject(obj);
                    dataProvider.InitSpriteEditorDataProvider();
    
                    /* Use the data provider */
    
                    // Apply the changes made to the data provider
                    dataProvider.Apply();
    
                    // Reimport the asset to have the changes applied
                    var assetImporter = dataProvider.targetObject as AssetImporter;
                    assetImporter.SaveAndReimport();
                }
            }
        }
    }
    

## How to add Sprites

    
    
    static void AddSprite(ISpriteEditorDataProvider dataProvider)
    {
        // Define the new Sprite Rect
        var newSprite = new SpriteRect()
        {
            name = "MyNewSprite",
            spriteID = GUID.Generate(),
            rect = new Rect(0, 0, 32, 32)
        };
        // Add the Sprite Rect to the list of existing Sprite Rects
        var spriteRects = dataProvider.GetSpriteRects().ToList();
        spriteRects.Add(newSprite);
    
        // Write the updated data back to the data provider
        dataProvider.SetSpriteRects(spriteRects.ToArray());
    
        // Note: This section is only for Unity 2021.2 and newer
        // Register the new Sprite Rect's name and GUID with the ISpriteNameFileIdDataProvider
        var spriteNameFileIdDataProvider = dataProvider.GetDataProvider<ISpriteNameFileIdDataProvider>();
        var nameFileIdPairs = spriteNameFileIdDataProvider.GetNameFileIdPairs().ToList();
        nameFileIdPairs.Add(new SpriteNameFileIdPair(newSprite.name, newSprite.spriteID));
        spriteNameFileIdDataProvider.SetNameFileIdPairs(nameFileIdPairs);
        // End of Unity 2021.2 and newer section
    
        // Apply the changes
        dataProvider.Apply();
    }
    

## How to change Sprite data

    
    
    static void SetPivot(ISpriteEditorDataProvider dataProvider)
    {
        // Get all the existing Sprites
        var spriteRects = dataProvider.GetSpriteRects();
    
        // Loop over all Sprites and update the pivots
        foreach (var rect in spriteRects)
        {
            rect.pivot = new Vector2(0.1f, 0.2f);
            rect.alignment = SpriteAlignment.Custom;
        }
    
        // Write the updated data back to the data provider
        dataProvider.SetSpriteRects(spriteRects);
    
        // Apply the changes
        dataProvider.Apply();
    }
    

## How to remove Sprites

    
    
    static void RemoveSprite(ISpriteEditorDataProvider dataProvider, string spriteName)
    {
        // Get all the existing Sprites and look for the Sprite with the selected name
        var spriteRects = dataProvider.GetSpriteRects().ToList();
        var index = spriteRects.FindIndex(x => x.name == spriteName);
    
        // Remove the entry of the Sprite if found
        if (index >= 0)
            spriteRects.RemoveAt(index);
    
        // Write the updated data back to the data provider
        dataProvider.SetSpriteRects(spriteRects.ToArray());
    
        // Note: This section is only for Unity 2021.2 and newer
        // Get all the existing SpriteName & FileId pairs and look for the Sprite with the selected name
        var spriteNameFileIdDataProvider = dataProvider.GetDataProvider<ISpriteNameFileIdDataProvider>();
        var nameFileIdPairs = spriteNameFileIdDataProvider.GetNameFileIdPairs().ToList();
        index = nameFileIdPairs.FindIndex(x => x.name == spriteName);
    
        // Remove the entry of the Sprite if found
        if (index >= 0)
            nameFileIdPairs.RemoveAt(index);
    
        spriteNameFileIdDataProvider.SetNameFileIdPairs(nameFileIdPairs);
        // End of Unity 2021.2 and newer section
    
        // Apply the changes
        dataProvider.Apply();
    }
    

## How to update Outline data

    
    
    static void SetOutline(ISpriteEditorDataProvider dataProvider)
    {
        // Get the ISpriteOutlineDataProvider
        var outlineDataProvider = dataProvider.GetDataProvider<ISpriteOutlineDataProvider>();
    
        // Loop over all Sprites and set their outline to a quad
        var spriteRects = dataProvider.GetSpriteRects();
        foreach (var spriteRect in spriteRects)
        {
            var halfWidth = spriteRect.rect.width / 2f;
            var halfHeight = spriteRect.rect.height / 2f;
    
            var quadOutline = new Vector2[4]
            {
                new Vector2(-halfWidth, -halfHeight),
                new Vector2(-halfWidth, halfHeight),
                new Vector2(halfWidth, halfHeight),
                new Vector2(halfWidth, -halfHeight)
            };
    
            var outlines = new List<Vector2[]>();
            outlines.Add(quadOutline);
    
            var spriteGuid = spriteRect.spriteID;
            outlineDataProvider.SetOutlines(spriteGuid, outlines);
        }
    
        // Apply the changes
        dataProvider.Apply();
    }
    

## Additional resources

  * Full list of available data providers in 2D Sprite package’s [Scripting API section](https://docs.unity3d.com/Packages/com.unity.2d.sprite@latest/index.html?subfolder=/api/UnityEditor.U2D.Sprites.html)

[](../../sprite/sprite-editor/secondary-texture/delete-secondary-texture.html)

Delete a secondary texture

[](../../sprite/sorting-group/sorting-group-landing.html)

Sorting groups

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://learn.unity.com/)[Community
Answers](https://answers.unity3d.com)[Knowledge
Base](https://support.unity3d.com/hc/en-
us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-
store)[Terms of
use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy
Policy](https://unity.com/legal/privacy-
policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share
My Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

