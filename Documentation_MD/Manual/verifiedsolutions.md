[](https://docs.unity3d.com)

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

Language : English

  * [English](/Manual/verifiedsolutions.html)
  * [中文](/cn/current/Manual/verifiedsolutions.html)
  * [日本語](/ja/current/Manual/verifiedsolutions.html)
  * [한국어](/kr/current/Manual/verifiedsolutions.html)

[](https://docs.unity3d.com)

## Unity Manual

Version: Unity 6Select a different version

Language : English

  * [English](/Manual/verifiedsolutions.html)
  * [中文](/cn/current/Manual/verifiedsolutions.html)
  * [日本語](/ja/current/Manual/verifiedsolutions.html)
  * [한국어](/kr/current/Manual/verifiedsolutions.html)

  * [Working in Unity](working-in-unity.html)
  * [Assets and media](assets-and-media.html)
  * [Unity's Asset Store](AssetStore.html)
  * Verified Solutions

[](AssetStoreAdmin.html)

Asset Store Publisher portal

[](verified-solutions-dt.html)

Decentralized technology Verified Solutions

# Verified Solutions

The Verified Solutions program is a library of third-party assets and
solutions that Unity curates. Unity evaluates these third-party offerings
based on how well the included assets enhance and extend the usability of core
Unity products. Unity technically verifies all offerings in the Verified
Solutions program to ensure compatibility with the most commonly used versions
of Unity.

For the Verified Solutions program, the Verified Solutions team at Unity:

  * Vets solutions thoroughly.
  * Evaluates solutions for quality and scalability, allowing many products to fulfill enterprise needs.
  * Reviews and gives feedback from Unity’s Release QA team members.
  * Allows solutions to be advertised as Verified Solutions and to include a Verified Solution badge on the **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) page, publisher website, marketing
materials, and so on.

  * Includes solutions in special collections, gives solutions prioritized listing on the Asset Store, and bestows special consideration for solutions to be included in Asset Store marketing and promotions.
  * Provides a dedicated support line to assist with onboarding.
  * Bestows special privileges in the Asset Store, including customized End User License Agreements (EULAs) and subscription- or consumption-based payment models.
  * In subscription-based payment models, you pay a recurring price at regular intervals for access to the product or service.
  * In consumption-based (pay-per-use) payment models, you pay based on resource usage.

**Note** : You, as the provider, certify that your solutions will work when
Unity is updated and address bugs in a timely manner.

## Process to become a Verified Solution

The Verified Solutions program exhibits tools and services that provide
additional functionality for Unity users. These products can, for example,
include software development kits (SDKs), plugins, and Editor extensions,
among other offerings. The Verified Solutions program is not suitable for
third-party products that only provide asset packs, such as 3D models, audio,
and **sprites** A 2D graphic objects. If you are used to working in 3D,
Sprites are essentially just standard textures but there are special
techniques for combining and managing sprite textures for efficiency and
convenience during development. [More info](sprite/sprite-landing.html)  
See in [Glossary](Glossary.html#Sprite).

### Requirements

To begin the verification process, solutions must fulfill the following
requirements.

#### Release-ready solution

The solution must be release-ready, which means the product:

  * Has passed all internal QA processes.
  * Is compliant with Unity’s Asset Store guidelines.
  * Is in a ready-to-release state.

Ready-to-release includes all aspects of the solution that the users interact
with while they use the product. For example, if the solution depends on
website interfaces to manage features, such as an administration portal, the
associated websites must be ready for consumer use. Any work-in-progress or
experimental features must be clearly marked and served separately from core
functionality. Users must be able to use all core functionality of the
solution independent from experimental features.

#### Detailed documentation

You must provide detailed and extensive documentation for the solution, which
must meet the following requirements:

  * Includes a list of supported Unity streams and platforms.
  * Outlines unsupported graphics pipelines (such as HDRP, URP, or Built-In) and **scripting backends** A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend) (such as Mono or IL2CPP).

  * Documents limitations or unusual setup procedures.
  * Details the integration process and all features available to the user, with examples when possible.
  * Documents all publicly available and intended-for-use APIs with descriptions of passed and returned parameters and all possible exceptions the user might encounter.
  * Provides examples of how core APIs are used.
  * Presents known issues and temporary workarounds.
  * Includes a changelog of product changes.
  * A changelog provides insight to customers and helps speed up the Verified Solutions verification process, especially if the solution needs to be re-verified.
  * The changelog should include descriptions of newly added and updated features, as well as any bug fixes that have been applied to each version.

Alongside online documentation, you must bundle the solution with one-page
summaries that encapsulate the main features offered by the solution and links
to the full online documentation and changelog. You can also provide an
offline version of the full documentation and the changelog for the currently
installed version of the product.

#### Clean solution structure

The solution must be in its own folder, which can help customers maintain an
organized project structure, especially when they use many third-party
products. Some solutions may need [special folders](SpecialFolders.html) that
require a certain path to work correctly. When a solution requires this file
structure, create a folder named after the solution inside the required
[special folder](SpecialFolders.html).

**Note** : Don’t include any unused assets in the product, and don’t bundle
internal development tools with the solution.

#### Clean code

All publicly accessible code must be clean and readable and meet the following
requirements:

  * Script structure and contents must use a unified style and follow a single naming convention.
  * All public-facing APIs must have summaries or comments.
  * Titles, descriptions, keywords, and code comments must be in English.

#### Demos and samples

You must provide demonstrations of features for new users. Demos are one of
the first ways new users can experience a new product, so demos are a crucial
way to give the user a great and lasting impression. If possible, bundle the
demo with the solution. If doing so significantly increases the size of the
product, you can provide the demo separately and refer to it in the
documentation.

Some solutions aren’t suited to a traditional demo or samples. For example,
some Editor extensions might work out of the box without any additional
integration. In these cases, you can provide a short video to introduce the
product to new users and help speed up the exploration phase of the Verified
Solutions verification process.

#### Compliance with the Asset Store submission guidelines

Before you apply to the Verified Solutions program, familiarize yourself with
the [Asset Store Submission
Guidelines](https://assetstore.unity.com/publishing/submission-guidelines).
Use the [Asset Store
Tools](https://assetstore.unity.com/packages/tools/utilities/asset-store-
publishing-tools-115) Validator tool to help comply with all applicable
guidelines.

![The Asset Store Validator tool scans your solution and provides feedback,
which includes detailed errors, warnings, and itemized passed
checks.](../uploads/Main/AssetStoreValidator.png) The Asset Store Validator
tool scans your solution and provides feedback, which includes detailed
errors, warnings, and itemized passed checks.

## Onboarding Process as a Verified Solution

### Process to submit solutions to the Verified Solutions team

Before the Verified Solutions team can start technical verification, you must
submit the following information:

  * A link to the solution
  * Size of the solution
  * Supported Unity versions
  * Supported platforms
  * Any necessary licensing files
  * Login information to any back-end services or administration consoles
  * A link to the documentation

You must also complete detailed internal QA procedures.

You must provide technical details through [this
form](https://airtable.com/shrrTKYkeNzeAEitJ).

### Technical verification process

The Verified Solutions team evaluates solutions in four stages:

  * Exploration
  * Verification
  * Report
  * Contact

You can read about each stage in detail below.

#### Exploration

The Verified Solutions team dedicates the beginning of the verification
process to understanding the solution. The team evaluates the solution to
determine its size and complexity. The team uses documentation and other
available learning resources (such as demos and tutorial videos) to understand
the solution and determine the core and most commonly used features. The team
uses this information to set up a new Unity project for the solution.

#### Verification

During this step, each core feature is thoroughly tested. The Verified
Solutions team creates automated tests to cover all core APIs and help with
any other areas that may require manual work. The team uses solution scope,
defined during the exploration phase, to determine whether more obscure APIs
and features can be reasonably tested in as much detail as the main features.
To make sure customers can trust the solution to work on any of the supported
platforms, the solution is comprehensively tested on each platform, beginning
with one Unity version. If a critical issue that prevents use of the partner
solution is discovered, the team halts verification and informs you of the
issue. Otherwise, the solution is then tested on all Unity LTS streams and the
latest Tech stream. The team verifies documentation during this step to make
sure that customers can find all the needed information regardless of their
level of experience with Unity services.

During the final step of the verification process, the Verified Solutions team
verifies the solution using the [Asset Store
Tools](https://assetstore.unity.com/packages/tools/utilities/asset-store-
publishing-tools-115) Validator. Although the Verified Solutions program
offers a custom end user license agreement (EULA), you must verify that the
solution you are submitting follows all applicable guidelines for Asset Store
Tools. The Verified Solutions team documents any issues found during the
verification process and details them during the report phase.

#### Report

After the Verified Solutions team tests the solution, they submit a
verification report that details insights found during the process.

The first page of the report details the core information about the solution,
such as:

  * The solution name
  * The version
  * Supported platforms

The summary section of the report includes:

  * An overview of past verifications
  * Exact Unity versions used
  * Test device information
  * Covered platforms
  * Test statistics

This section provides a quick view of the outcome of the report and highlights
important issues alongside other notes and suggestions from Unity that could
improve the overall user experience.

![The first section of the verification report includes information about
submission dates, data, and testing summaries for the verified
solution.](../uploads/Main/VerifiedSolutionsReportExample1.png) The first
section of the verification report includes information about submission
dates, data, and testing summaries for the verified solution.

The next section of the report contains the detailed information on each test
case:

  * Description
  * General status of the test case and platform-specific statuses, which detail whether any related issues were found
  * Comments that detail any found issues, affected Unity streams, reproduction steps, and any other relevant notes
  * Severity of found issues

![The second section of the verification report includes an itemized list of
the performed tests, whether the solution passed or failed these tests, and
comments and bug severity ratings from the Unity testing
team.](../uploads/Main/VerifiedSolutionsReportExample2.png) The second section
of the verification report includes an itemized list of the performed tests,
whether the solution passed or failed these tests, and comments and bug
severity ratings from the Unity testing team.

The report categorizes issues found during the verification phase by severity
using the following categories:

  * Minor: Non-core or niche features don’t function as expected; warnings are not user friendly; non-breaking errors or exceptions display; or the feature has cosmetic issues that don’t hinder the usability of the feature.
  * Major: Core solution features don’t function as expected; the Unity Editor or Unity Player crashes, which results in a loss of progress or data; or errors are commonly and continuously encountered.
  * Critical: The solution is unusable due to issues; the solution doesn’t work with primary target platforms; or the solution includes issues that risk causing problems to the operating system as well as Unity products.

To receive approval as a Verified Solution, a product can’t contain any major
or critical issues.

Other Verified Solutions team members review the completed verification report
to ensure all issues are categorized correctly and that the report is accurate
and complete.

#### Verification results

If the Verified Solutions team found major or critical issues in the solution
during the verification process, you must fix these issues before the Verified
Solutions team can reverify the solution. When the team completes
verification, they send the solution to the Verified Solutions publisher, and
the product is officially recognized as a Verified Solution.

## Asset Store account creation and upload

For more information about how to create an Asset Store account and upload
solutions, please refer to the [Unity manual](AssetStorePublishing.html).

### Custom EULA

You can distribute a Verified Solution through the Unity Asset Store with
either the standard Asset Store end user license agreement (EULA) or a custom
EULA. The standard Unity Asset Store EULA is appropriate for asset type
packages, including 3D and **2D objects** A 2D GameObject such as a tilemap or
sprite. [More info](Unity2D.html)  
See in [Glossary](Glossary.html#2DObject), game templates, and audio packs.
Tool- or SDK-type packages may require specific additional information in the
EULA.

To include a custom EULA, add a sentence to the description of the solution
stating the following: “This asset is governed by the <provider’s name> EULA
<link>.” You must email the Verified Solutions team at vs-support@unity3d.com
regarding the custom EULA.

## Unity.com Verified Solutions page

The Verified Solutions team adds all Verified Solutions to the
[business](https://unity.com/partners/verified-solutions) and [creator
pages](https://unity.com/partners/verified-solutions-for-creators) on the
Asset Store website ([assetstore.unity.com](https://assetstore.unity.com)).

You must submit the following information to the Verified Solutions team
before your solution is added to the Unity.com website:

  * A logo of the company or solution as an .EPS or .AI file, as well as a white version on a transparent background for the black background
  * A product image with a horizontal layout in 16:9 aspect ratio
  * Text that describes the company or solution in 50 words or fewer (30–40 words is preferred) You must submit assets through this [questionnaire form](https://airtable.com/shrrpCDiBGYn6otqY).

## Support for Verified Solutions

If you need general or technical support, or if you have any questions about
the Verified Solutions program, please email the Unity Verified Solutions team
at [vs-support@unity3d.com](mailto:vs-support@unity3d.com].

## Additional communication guidelines for Verified Solutions

  * Information specific to [Verified Solutions for decentralized technologies](verified-solutions-dt.html)
  * Use of badging: [How to link to the Unity Brand Page](https://brandguide.brandfolder.com/unity/downloadbrandassets)

[](AssetStoreAdmin.html)

Asset Store Publisher portal

[](verified-solutions-dt.html)

Decentralized technology Verified Solutions

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

