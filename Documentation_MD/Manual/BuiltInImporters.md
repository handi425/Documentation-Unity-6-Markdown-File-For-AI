[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/BuiltInImporters.html)
  * [中文](/cn/current/Manual/BuiltInImporters.html)
  * [日本語](/ja/current/Manual/BuiltInImporters.html)
  * [한국어](/kr/current/Manual/BuiltInImporters.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/BuiltInImporters.html)
  * [中文](/cn/current/Manual/BuiltInImporters.html)
  * [日本語](/ja/current/Manual/BuiltInImporters.html)
  * [한국어](/kr/current/Manual/BuiltInImporters.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [Supported Asset Types](AssetTypes.html)
  * Built-in Importers

[](AssetTypes.html)

Supported Asset Types

[](ScriptedImporters.html)

Scripted Importers

# Built-in Importers

Unity supports many asset file types via its collection of built-in importers.
Most of these importers are implemented in the Unity Editor’s native code, and
are named “native importers”. They provide the import functionality for most
of Unity’s basic asset types, such as 3D models, Textures, and audio files.

## Built in native importers

Importer | File Formats  
---|---  
AssemblyDefinitionImporter | asmdef  
AssemblyDefinitionReferenceImporter | asmref  
AudioImporter | ogg, aif, aiff, flac, wav, mp3, mod, it, s3m, xm  
ComputeShaderImporter | compute  
DefaultImporter | rsp, unity  
FBXImporter | fbx, mb, ma, max, jas, dae, dxf, obj, c4d, blend, lxo  
IHVImageFormatImporter | astc, dds, ktx, pvr  
LocalizationImporter | po  
Mesh3DSImporter | 3ds  
NativeFormatImporter | anim, animset, asset, blendtree, buildreport, colors, controller, **cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap), curves, curvesNormalized, flare,
fontsettings, giparams, gradients, guiskin, ht, mask, mat, **mesh** The main
graphics primitive of Unity. Meshes make up a large part of your 3D worlds.
Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms,
Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh), mixer, overrideController,
particleCurves, particleCurvesSigned, particleDoubleCurves,
particleDoubleCurvesSigned, physicMaterial, physicsMaterial2D, playable,
preset, renderTexture, shadervariants, spriteatlas, state, statemachine,
texture2D, transition, webCamTexture, brush, terrainlayer, signal  
PackageManifestImporter | json  
PluginImporter | dll, winmd, so, jar, java, kt, aar, suprx, prx, rpl, cpp, cc, c, h, jslib, jspre, bc, a, m, mm, swift, xib, bundle, dylib, config  
PrefabImporter | **prefab** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#Prefab)  
RayTracingShaderImporter | raytrace  
ShaderImporter | cginc, cg, glslinc, hlsl, **shader** A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#Shader)  
SketchUpImporter | skp  
SpeedTreeImporter | spm, st  
SubstanceImporter | .sbsar  
TextScriptImporter | txt, html, htm, xml, json, csv, yaml, bytes, fnt, manifest, md, js, boo, rsp  
TextureImporter | jpg, jpeg, tif, tiff, tga, gif, png, psd, bmp, iff, pict, pic, pct, exr, **hdr** high dynamic range  
See in [Glossary](Glossary.html#HDR)  
TrueTypeFontImporter | ttf, dfont, otf, ttc  
VideoClipImporter | avi, asf, wmv, mov, dv, mp4, m4v, mpg, mpeg, ogv, vp8, webm  
VisualEffectImporter | vfx, vfxoperator, vfxblock  
  
## Built-in scripted importers

[Scripted importers](ScriptedImporters.html) allow you to write your own
custom importers for formats that Unity does not natively support. However, in
addition to the built-in native importers listed above, some of Unity’s own
built-in importers are themselves implemented as scripted importers. This is
because they are implemented in C# in core packages, rather than within the
Editor’s native code itself. Unity imports scripted importer assets after
native importer assets.

Importer | File Formats  
---|---  
SpeedTree9Importer | .st9  
StyleSheetImporter | .uss  
UIElementsViewImporter | .uxml  
  
[](AssetTypes.html)

Supported Asset Types

[](ScriptedImporters.html)

Scripted Importers

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

