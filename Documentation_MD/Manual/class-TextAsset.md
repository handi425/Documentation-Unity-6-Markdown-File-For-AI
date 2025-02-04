[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/class-TextAsset.html)
  * [中文](/cn/current/Manual/class-TextAsset.html)
  * [日本語](/ja/current/Manual/class-TextAsset.html)
  * [한국어](/kr/current/Manual/class-TextAsset.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/class-TextAsset.html)
  * [中文](/cn/current/Manual/class-TextAsset.html)
  * [日本語](/ja/current/Manual/class-TextAsset.html)
  * [한국어](/kr/current/Manual/class-TextAsset.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Asset workflow](AssetWorkflow.html)
  * [Supported Asset Types](AssetTypes.html)
  * Text assets

[](ImporterConsistency.html)

Importer Consistency

[](AssetMetadata.html)

Asset Metadata

# Text assets

[Switch to Scripting](../ScriptReference/TextAsset.html "Go to TextAsset page
in the Scripting Reference")

**Text Assets** are a format for imported text files. When you drop a text
file into your Project Folder, it will be converted to a Text Asset. The
supported text formats are:

  * **.txt**
  * **.html**
  * **.htm**
  * **.xml**
  * **.bytes**
  * **.json**
  * **.csv**
  * **.yaml**
  * **.fnt**
  * **.md**

_Note that script files are also considered text assets for the purposes of
using
the[AssetDatabase.FindAssets](../ScriptReference/AssetDatabase.FindAssets.html)
function, so they will also be included in the list of results when this
function is used with the “t:TextAsset” filter._

![The Text Asset Inspector](../uploads/Main/TextAssetInspector.png) The Text
Asset Inspector

## Properties

**_Property:_** | **_Function:_**  
---|---  
**Text** A non-interactive piece of text to the user. This can be used to
provide captions or labels for other GUI controls or to display instructions
or other text. [More
info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-
Text.html)  
See in [Glossary](Glossary.html#Text) | The full text of the asset as a single string.  
  
## Details

The Text Asset is a very specialized use case. It is extremely useful for
getting text from different text files into your game while you are building
it. You can write up a simple .txt file and bring the text into your game very
easily. It is not intended for text file generation at runtime. For that you
will need to use traditional Input/Output programming techniques to read and
write external files.

Consider the following scenario. You are making a traditional text-heavy
adventure game. For production simplicity, you want to break up all the text
in the game into the different rooms. In this case you would make one text
file that contains all the text that will be used in one room. From there it
is easy to make a reference to the correct Text Asset for the room you enter.
Then with some customized parsing logic, you can manage a large amount of text
very easily.

### Binary data

A special feature of the text asset is that it can be used to store binary
data. By giving a file the extension **.bytes** it can be loaded as a text
asset and the data can be accessed through the **bytes** property.

For example put a jpeg file into the Resources folder and change the extension
to **.bytes** , then use the following script code to read the data at
runtime:

    
    
    //Load texture from disk
    TextAsset bindata = Resources.Load("Texture") as TextAsset;
    Texture2D tex = new Texture2D(1,1);
    tex.LoadImage(bindata.bytes); 
    

Please notice that files with the **.txt** and **.bytes** extension will be
treated as text and binary files, respectively. Do not attempt to store a
binary file using the **.txt** extension, as this will create unexpected
behaviour when attempting to read data from it.

## Hints

  * Text Assets are serialized like all other assets in a build. There is no physical text file included when you publish your game.
  * Text Assets are not intended to be used for text file generation at runtime.

TextAsset

[](ImporterConsistency.html)

Importer Consistency

[](AssetMetadata.html)

Asset Metadata

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

